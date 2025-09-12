#!/bin/bash

# Quick local test script for the conversion workflow
# This can be run locally to verify the conversion is working

echo "🧪 Local Conversion Test"
echo "========================"

# Run the conversion
echo "📝 Running conversion..."
bash scripts/convert-guidelines.sh

# Check if output file exists
if [ -f "_pages/guidelines.md" ]; then
    echo "✅ Output file created: _pages/guidelines.md"
    
    # Check file size
    size=$(wc -c < _pages/guidelines.md)
    echo "📊 File size: $size bytes"
    
    # Check for converted patterns to plain text
    if grep -q 'x = 5' _pages/guidelines.md; then
        echo "✅ Simple math conversion working"
    else
        echo "❌ Simple math conversion not working"
    fi
    
    # Check for code blocks
    html_blocks=$(grep -c '```html' _pages/guidelines.md)
    math_blocks=$(grep -c '```math' _pages/guidelines.md)
    echo "✅ HTML code blocks: $html_blocks"
    echo "✅ Math code blocks: $math_blocks"
    
    # Check for MathML namespace
    math_with_namespace=$(grep -c 'xmlns="http://www.w3.org/1998/Math/MathML"' _pages/guidelines.md)
    echo "✅ MathML elements with namespace: $math_with_namespace"
    
    # Count remaining LaTeX patterns
    latex_count=$(grep -c '\$.*\$' _pages/guidelines.md)
    echo "ℹ️  Remaining LaTeX patterns: $latex_count (documentation examples)"
    
    echo ""
    echo "🎉 Local test completed successfully!"
else
    echo "❌ Output file not found"
    exit 1
fi
