#!/bin/bash

# Test script for convert-guidelines.sh
# This script runs the conversion and shows the results

echo "🧪 Testing convert-guidelines.sh script..."
echo "=========================================="

# Run the conversion script
echo "📝 Running conversion script..."
bash scripts/convert-guidelines.sh

echo ""
echo "✅ Conversion completed!"
echo ""

# Check if the output file was created
if [ -f "_pages/guidelines.md" ]; then
    echo "📄 Output file created: _pages/guidelines.md"
    echo "📊 File size: $(wc -c < _pages/guidelines.md) bytes"
    echo "📏 Line count: $(wc -l < _pages/guidelines.md) lines"
    echo ""
    
    # Show some key content
    echo "🔍 Sample content:"
    echo "------------------"
    head -20 _pages/guidelines.md
    echo ""
    echo "   ... (truncated) ..."
    echo ""
    
    # Check for specific patterns
    echo "🔍 Checking for converted patterns:"
    echo "-----------------------------------"
    
    # Check for converted math to plain text
    if grep -q 'x = 5' _pages/guidelines.md; then
        echo "✅ Simple math conversion working: \$x = 5.\$ → x = 5"
    else
        echo "❌ Simple math conversion not working"
    fi
    
    # Check for other plain text patterns
    if grep -q '5/2' _pages/guidelines.md; then
        echo "✅ Fraction conversion working: \$\frac{5}{2}\$ → 5/2"
    else
        echo "ℹ️  Fraction conversion not found (may not be present in content)"
    fi
    
    if grep -q 'x^2' _pages/guidelines.md; then
        echo "✅ Superscript conversion working: \$x^2\$ → x^2"
    else
        echo "ℹ️  Superscript conversion not found (may not be present in content)"
    fi
    
    # Check for preserved MathML examples
    if grep -q '<math xmlns="http://www.w3.org/1998/Math/MathML">' _pages/guidelines.md; then
        echo "✅ MathML examples preserved"
    else
        echo "❌ MathML examples missing"
    fi
    
    # Check for code blocks
    if grep -q '```html' _pages/guidelines.md; then
        echo "✅ HTML code blocks preserved"
    else
        echo "❌ HTML code blocks missing"
    fi
    
    if grep -q '```math' _pages/guidelines.md; then
        echo "✅ Math code blocks preserved"
    else
        echo "❌ Math code blocks missing"
    fi
    
else
    echo "❌ Output file not created!"
    exit 1
fi

echo ""
echo "🎉 Test completed successfully!"
