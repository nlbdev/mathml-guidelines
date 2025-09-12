#!/bin/bash

# Script to convert Nordic MathML Guidelines markdown to Jekyll page
# This script is run during the GitHub Actions build process

set -e

# Create the _pages directory if it doesn't exist
mkdir -p _pages

# Create the guidelines page with proper front matter
cat > _pages/guidelines.md << 'EOF'
---
layout: page
title: Nordic Guidelines for Mathematical Content in HTML Files, Using MathML
description: Comprehensive guidelines for creating accessible mathematical content using MathML
permalink: /
---

EOF

# Process the markdown file to fix common issues
if [ -f "Nordic MathML Guidelines.md" ]; then
    # Create a temporary file for processing
    temp_file=$(mktemp)
    
    # Copy content skipping the first line (title)
    tail -n +2 "Nordic MathML Guidelines.md" > "$temp_file"
    
    # Use Python script to convert LaTeX math to MathML
    if command -v python &> /dev/null; then
        python scripts/convert-mathml.py "$temp_file" "$temp_file"
    else
        echo "Warning: Python not found, using basic sed processing"
        # Fallback to basic sed processing
        sed -i 's/```html/```html/g' "$temp_file"
        sed -i 's/```math/```math/g' "$temp_file"
        sed -i 's/<math>/<math xmlns="http:\/\/www.w3.org\/1998\/Math\/MathML">/g' "$temp_file"
    fi
    
    # Append the processed content
    cat "$temp_file" >> _pages/guidelines.md
    
    # Clean up temporary file
    rm "$temp_file"
    
    echo "Successfully converted Nordic MathML Guidelines to Jekyll page"
else
    echo "Error: Nordic MathML Guidelines.md not found"
    exit 1
fi