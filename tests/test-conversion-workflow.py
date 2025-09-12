#!/usr/bin/env python3
"""
Test script for verifying the MathML conversion workflow.
This script can be run in GitHub Actions to validate the conversion output.
"""

import os
import re
import sys
from pathlib import Path

def test_file_exists(file_path, description):
    """Test if a file exists and return status."""
    if os.path.exists(file_path):
        print(f"✅ {description}: {file_path}")
        return True
    else:
        print(f"❌ {description}: {file_path} - FILE NOT FOUND")
        return False

def test_file_size(file_path, min_size=1000):
    """Test if file has reasonable size."""
    if not os.path.exists(file_path):
        return False
    
    size = os.path.getsize(file_path)
    if size >= min_size:
        print(f"✅ File size: {size} bytes (>= {min_size})")
        return True
    else:
        print(f"❌ File size: {size} bytes (< {min_size})")
        return False

def test_plain_text_conversion(file_path):
    """Test if LaTeX patterns have been converted to plain text."""
    if not os.path.exists(file_path):
        return False
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Test for converted simple math patterns to plain text
    plain_text_patterns = [
        r'x = 5',  # Simple equation
        r'5/2',    # Simple fraction
        r'√9 = 3', # Square root
        r'x\^2',   # Superscript
        r'x_i',    # Subscript
    ]
    
    conversions_found = 0
    for pattern in plain_text_patterns:
        if re.search(pattern, content):
            conversions_found += 1
            print(f"✅ Found converted pattern: {pattern}")
    
    if conversions_found > 0:
        print(f"✅ Plain text conversions: {conversions_found} patterns converted")
        return True
    else:
        print("❌ No plain text conversions found")
        return False

def test_mathml_namespace(file_path):
    """Test if MathML elements have proper namespace."""
    if not os.path.exists(file_path):
        return False
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Count MathML elements with and without namespace
    math_with_namespace = len(re.findall(r'<math xmlns="http://www.w3.org/1998/Math/MathML">', content))
    math_without_namespace = len(re.findall(r'<math>(?!\s*xmlns)', content))
    
    print(f"✅ MathML elements with namespace: {math_with_namespace}")
    if math_without_namespace > 0:
        print(f"⚠️  MathML elements without namespace: {math_without_namespace}")
    else:
        print("✅ All MathML elements have namespace")
    
    return math_without_namespace == 0

def test_code_blocks(file_path):
    """Test if code blocks are properly formatted."""
    if not os.path.exists(file_path):
        return False
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check for properly formatted code blocks
    html_blocks = len(re.findall(r'```html', content))
    math_blocks = len(re.findall(r'```math', content))
    
    print(f"✅ HTML code blocks: {html_blocks}")
    print(f"✅ Math code blocks: {math_blocks}")
    
    return html_blocks > 0 and math_blocks > 0

def test_preserved_mathml(file_path):
    """Test if existing MathML examples are preserved."""
    if not os.path.exists(file_path):
        return False
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Look for preserved MathML examples (should have proper structure)
    preserved_examples = len(re.findall(r'<math xmlns="http://www.w3.org/1998/Math/MathML">\s*<mi>x</mi>\s*<mo>=</mo>\s*<mn>5</mn>\s*<mtext>\.</mtext>\s*</math>', content))
    
    if preserved_examples > 0:
        print(f"✅ Preserved MathML examples: {preserved_examples}")
        return True
    else:
        print("❌ No preserved MathML examples found")
        return False

def test_remaining_latex(file_path):
    """Test how many LaTeX patterns remain (should be documentation examples)."""
    if not os.path.exists(file_path):
        return False
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Count remaining LaTeX patterns
    latex_patterns = len(re.findall(r'\$[^$]+\$', content))
    
    print(f"ℹ️  Remaining LaTeX patterns: {latex_patterns}")
    
    # These should be documentation examples, not conversion failures
    if latex_patterns <= 30:  # Reasonable number for documentation examples
        print("✅ Reasonable number of LaTeX patterns (likely documentation examples)")
        return True
    else:
        print("⚠️  High number of LaTeX patterns - may indicate conversion issues")
        return False

def main():
    """Run all tests."""
    print("🧪 Testing LaTeX to Plain Text Conversion Workflow")
    print("=" * 50)
    
    # Test file path
    guidelines_file = "_pages/guidelines.md"
    
    # Run tests
    tests = [
        ("File exists", lambda: test_file_exists(guidelines_file, "Guidelines file")),
        ("File size", lambda: test_file_size(guidelines_file)),
        ("Plain text conversion", lambda: test_plain_text_conversion(guidelines_file)),
        ("MathML namespace", lambda: test_mathml_namespace(guidelines_file)),
        ("Code blocks", lambda: test_code_blocks(guidelines_file)),
        ("Preserved MathML", lambda: test_preserved_mathml(guidelines_file)),
        ("Remaining LaTeX", lambda: test_remaining_latex(guidelines_file)),
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n📋 {test_name}:")
        try:
            if test_func():
                passed += 1
        except Exception as e:
            print(f"❌ Error in {test_name}: {e}")
    
    print(f"\n📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! Conversion workflow is working correctly.")
        return 0
    else:
        print("⚠️  Some tests failed. Please check the conversion script.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
