# Test Files

This directory contains test files for verifying the MathML conversion workflow.

## Files

### `test-conversion-workflow.py`

**Purpose**: Comprehensive testing for GitHub Actions CI/CD pipeline
**Usage**: `python tests/test-conversion-workflow.py`
**Features**:

- File existence and size validation
- MathML conversion verification
- MathML namespace checking
- Code block formatting validation
- Preserved MathML examples verification
- LaTeX pattern counting (for documentation examples)
- Detailed reporting with pass/fail status

### `test-local.sh`

**Purpose**: Quick local verification
**Usage**: `bash tests/test-local.sh`
**Features**:

- Runs conversion script
- Basic validation checks
- Simple reporting
- Fast execution

### `test-conversion.sh`

**Purpose**: Comprehensive local testing with detailed output
**Usage**: `bash tests/test-conversion.sh`
**Features**:

- Runs conversion script
- Detailed validation checks
- Sample content display
- Pattern verification
- Comprehensive reporting

## Running Tests

### Local Testing

```bash
# Quick test
bash tests/test-local.sh

# Comprehensive test
bash tests/test-conversion.sh

# Python test
python tests/test-conversion-workflow.py
```

### CI/CD Testing

The `test-conversion-workflow.py` script runs automatically in the GitHub Actions workflow after the conversion step and before the Jekyll build step.

## Test Results

All tests should pass for a successful conversion:

- ✅ File generation
- ✅ MathML conversion
- ✅ Namespace validation
- ✅ Code block formatting
- ✅ Documentation preservation
- ✅ LaTeX pattern counting
