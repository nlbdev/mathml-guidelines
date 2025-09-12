#!/usr/bin/env python3
"""
Script to convert LaTeX math syntax to plain text in markdown files.
This script handles the conversion of dollar-sign math to plain text format.
"""

import re
import sys
import os

def convert_latex_to_mathml(latex_expr):
    """
    Convert simple LaTeX expressions to plain text.
    This is a basic converter for common patterns.
    """
    # Handle simple variables and numbers
    latex_expr = latex_expr.strip()
    
    # Basic patterns for common math expressions
    patterns = [
        # Fractions: \frac{a}{b} -> <mfrac><mn>a</mn><mn>b</mn></mfrac>
        (r'\\frac\{([^}]+)\}\{([^}]+)\}', r'<mfrac><mn>\1</mn><mn>\2</mn></mfrac>'),
        
        # Superscripts: x^2 -> <msup><mi>x</mi><mn>2</mn></msup>
        (r'([a-zA-Z])\^(\d+)', r'<msup><mi>\1</mi><mn>\2</mn></msup>'),
        
        # Subscripts: x_i -> <msub><mi>x</mi><mi>i</mi></msub>
        (r'([a-zA-Z])_(\w+)', r'<msub><mi>\1</mi><mi>\2</mi></msub>'),
        
        # Square root: \sqrt{x} -> <msqrt><mi>x</mi></msqrt>
        (r'\\sqrt\{([^}]+)\}', r'<msqrt><mi>\1</mi></msqrt>'),
        
        # Text in math: \text{text} -> <mtext>text</mtext>
        (r'\\text\{([^}]+)\}', r'<mtext>\1</mtext>'),
        
        # Greek letters and common symbols
        (r'\\bar\{([^}]+)\}', r'<mover><mi>\1</mi><mo>&#8254;</mo></mover>'),
        (r'\\hat\{([^}]+)\}', r'<mover><mi>\1</mi><mo>^</mo></mover>'),
        (r'\\vec\{([^}]+)\}', r'<mover><mi>\1</mi><mo>→</mo></mover>'),
        
        # Operators
        (r'\\rightarrow', r'<mo>→</mo>'),
        (r'\\leftarrow', r'<mo>←</mo>'),
        (r'\\pm', r'<mo>±</mo>'),
        (r'\\mp', r'<mo>∓</mo>'),
        (r'\\times', r'<mo>×</mo>'),
        (r'\\div', r'<mo>÷</mo>'),
        (r'\\leq', r'<mo>≤</mo>'),
        (r'\\geq', r'<mo>≥</mo>'),
        (r'\\neq', r'<mo>≠</mo>'),
        (r'\\approx', r'<mo>≈</mo>'),
        (r'\\infty', r'<mo>∞</mo>'),
        (r'\\sum', r'<mo>∑</mo>'),
        (r'\\int', r'<mo>∫</mo>'),
        (r'\\prod', r'<mo>∏</mo>'),
        (r'\\alpha', r'<mi>α</mi>'),
        (r'\\beta', r'<mi>β</mi>'),
        (r'\\gamma', r'<mi>γ</mi>'),
        (r'\\delta', r'<mi>δ</mi>'),
        (r'\\epsilon', r'<mi>ε</mi>'),
        (r'\\theta', r'<mi>θ</mi>'),
        (r'\\lambda', r'<mi>λ</mi>'),
        (r'\\mu', r'<mi>μ</mi>'),
        (r'\\pi', r'<mi>π</mi>'),
        (r'\\sigma', r'<mi>σ</mi>'),
        (r'\\tau', r'<mi>τ</mi>'),
        (r'\\phi', r'<mi>φ</mi>'),
        (r'\\omega', r'<mi>ω</mi>'),
    ]
    
    # Apply patterns
    for pattern, replacement in patterns:
        latex_expr = re.sub(pattern, replacement, latex_expr)
    
    # Handle simple variables (single letters that aren't already in MathML)
    latex_expr = re.sub(r'\b([a-zA-Z])\b(?!\s*[<>])', r'<mi>\1</mi>', latex_expr)
    
    # Handle numbers
    latex_expr = re.sub(r'\b(\d+(?:\.\d+)?)\b', r'<mn>\1</mn>', latex_expr)
    
    # Handle operators
    latex_expr = re.sub(r'([+\-*/=<>])', r'<mo>\1</mo>', latex_expr)
    
    # Handle parentheses
    latex_expr = re.sub(r'([()])', r'<mo>\1</mo>', latex_expr)
    
    return latex_expr

def process_markdown_file(input_file, output_file):
    """
    Process the markdown file to convert LaTeX math to plain text.
    This script ONLY converts LaTeX syntax ($...$) to plain text, 
    it does NOT modify existing MathML markup which is used for documentation.
    """
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Add MathML namespace to existing math elements that don't have it
    # Only match <math> tags that are actual HTML elements (not in text content)
    # Look for <math> followed by whitespace and then a tag like <mi>, <mo>, etc.
    content = re.sub(r'<math>(?=\s*<(?:mi|mo|mn|mfrac|msup|msub|msqrt|mroot|mover|munder|mtext|mrow|mtable|mtr|mtd))', '<math xmlns="http://www.w3.org/1998/Math/MathML">', content)
    
    # Also handle <math> tags that might be on the same line or have attributes
    content = re.sub(r'<math(?![^>]*xmlns)(?=\s*[^>]*>)', '<math xmlns="http://www.w3.org/1998/Math/MathML"', content)
    
    # Convert display math $$...$$ to code blocks (this is safe)
    content = re.sub(r'\$\$([^$]+)\$\$', r'```math\n\1\n```', content)
    
    # Fix code block formatting - these should already be correct, but let's ensure they are
    # No changes needed for code blocks as they should already be properly formatted
    
    # Only convert simple LaTeX patterns that are clearly not part of existing MathML
    # We'll be very conservative and only convert the most obvious cases
    
    # Convert simple inline math like $x = 5$ to plain text but NOT if it's inside existing <math> tags
    def convert_simple_math(match):
        math_expr = match.group(1)
        
        # Check if this is inside existing MathML tags by looking backwards
        before_text = content[:match.start()]
        
        # Find the last unclosed <math> tag before this position
        last_math_start = before_text.rfind('<math')
        last_math_end = before_text.rfind('</math>')
        
        # If there's an unclosed <math> tag, don't convert
        if last_math_start > last_math_end:
            return match.group(0)
        
        # Convert various LaTeX patterns to plain text
        math_expr_clean = math_expr.strip()
        
        # Simple equations like x = 5
        if re.match(r'^[a-zA-Z]\s*=\s*\d+\.?$', math_expr_clean):
            var_name = math_expr_clean.split("=")[0].strip()
            value = math_expr_clean.split("=")[1].strip().rstrip(".")
            return f'{var_name} = {value}'
        
        # Simple fractions like \frac{5}{2}
        if re.match(r'^\\frac\{([^}]+)\}\{([^}]+)\}$', math_expr_clean):
            match_frac = re.match(r'^\\frac\{([^}]+)\}\{([^}]+)\}$', math_expr_clean)
            num = match_frac.group(1)
            den = match_frac.group(2)
            return f'{num}/{den}'
        
        # Fractions with text like \frac{\text{m}}{\text{s}^2}
        if re.match(r'^\\frac\{\\text\{([^}]+)\}\}\{\\text\{([^}]+)\}\^(\d+)\}$', math_expr_clean):
            match_frac_text = re.match(r'^\\frac\{\\text\{([^}]+)\}\}\{\\text\{([^}]+)\}\^(\d+)\}$', math_expr_clean)
            num_text = match_frac_text.group(1)
            den_text = match_frac_text.group(2)
            den_sup = match_frac_text.group(3)
            return f'{num_text}/{den_text}^{den_sup}'
        
        # Simple superscripts like x^2
        if re.match(r'^([a-zA-Z])\^(\d+)$', math_expr_clean):
            match_sup = re.match(r'^([a-zA-Z])\^(\d+)$', math_expr_clean)
            base = match_sup.group(1)
            exp = match_sup.group(2)
            return f'{base}^{exp}'
        
        # Simple subscripts like x_i
        if re.match(r'^([a-zA-Z])_([a-zA-Z])$', math_expr_clean):
            match_sub = re.match(r'^([a-zA-Z])_([a-zA-Z])$', math_expr_clean)
            base = match_sub.group(1)
            sub = match_sub.group(2)
            return f'{base}_{sub}'
        
        # Square roots like \sqrt{9} = 3
        if re.match(r'^\\sqrt\{([^}]+)\}\s*=\s*(\d+)$', math_expr_clean):
            match_sqrt = re.match(r'^\\sqrt\{([^}]+)\}\s*=\s*(\d+)$', math_expr_clean)
            radicand = match_sqrt.group(1)
            result = match_sqrt.group(2)
            return f'√{radicand} = {result}'
        
        # Square roots with index like \sqrt[3]{9} = 2
        if re.match(r'^\\sqrt\[(\d+)\]\{([^}]+)\}\s*=\s*(\d+)$', math_expr_clean):
            match_root = re.match(r'^\\sqrt\[(\d+)\]\{([^}]+)\}\s*=\s*(\d+)$', math_expr_clean)
            index = match_root.group(1)
            radicand = match_root.group(2)
            result = match_root.group(3)
            return f'^{index}√{radicand} = {result}'
        
        # Binomial like \binom{n}{k}
        if re.match(r'^\\binom\{([^}]+)\}\{([^}]+)\}$', math_expr_clean):
            match_binom = re.match(r'^\\binom\{([^}]+)\}\{([^}]+)\}$', math_expr_clean)
            n = match_binom.group(1)
            k = match_binom.group(2)
            return f'({n} choose {k})'
        
        # Text in math like \text{NaCl}
        if re.match(r'^\\text\{([^}]+)\}$', math_expr_clean):
            match_text = re.match(r'^\\text\{([^}]+)\}$', math_expr_clean)
            text = match_text.group(1)
            return text
        
        # For other patterns, just return as-is to avoid breaking documentation
        return match.group(0)
    
    # Apply the conservative conversion
    content = re.sub(r'\$([^$]+)\$', convert_simple_math, content)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 convert-mathml.py <input_file> <output_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' not found")
        sys.exit(1)
    
    process_markdown_file(input_file, output_file)
    print(f"Successfully processed {input_file} -> {output_file}")
