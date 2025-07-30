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
permalink: /guidelines/
---

EOF

# Append the content from the original markdown file, skipping the first line (title)
if [ -f "Nordic MathML Guidelines.md" ]; then
    tail -n +2 "Nordic MathML Guidelines.md" >> _pages/guidelines.md
    echo "Successfully converted Nordic MathML Guidelines to Jekyll page"
else
    echo "Error: Nordic MathML Guidelines.md not found"
    exit 1
fi