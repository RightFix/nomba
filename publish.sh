#!/bin/bash
# =============================================================================
# Script to build, test, and publish the nomba package to PyPI
# =============================================================================
#
# Usage:
#   ./publish.sh          # Build, test (dry-run), and publish to PyPI
#   ./publish.sh build    # Only build the package
#   ./publish.sh test    # Build and test upload to Test PyPI
#   ./publish.sh publish # Build and publish to main PyPI
#
# Requirements:
#   - uv (for building): https://github.com/astral-sh/uv
#   - twine (for uploading): pip install twine
#   - .pypirc file with PyPI credentials
#
# Steps:
#   1. Clean any previous builds from dist/
#   2. Build the wheel using uv
#   3. (Optional) Test upload to Test PyPI
#   4. Publish to main PyPI
#
# =============================================================================

set -e

COMMAND="${1:-all}"

clean_dist() {
    echo "Cleaning dist/ directory..."
    rm -rf dist/
}

build() {
    echo "Building package with uv..."
    uv build --wheel
    echo "Build complete. Output in dist/"
}

test_upload() {
    echo "Testing upload to Test PyPI..."
    twine upload --repository-url https://test.pypi.org/legacy/ dist/*
    echo "Test upload complete. Check https://test.pypi.org/project/nomba/"
}

publish() {
    echo "Publishing to PyPI..."
    twine upload dist/*
    echo "Published! Check https://pypi.org/project/nomba/"
}

case "$COMMAND" in
    build)
        clean_dist
        build
        ;;
    test)
        clean_dist
        build
        test_upload
        ;;
    publish)
        clean_dist
        build
        publish
        ;;
    all)
        clean_dist
        build
        echo ""
        echo "Ready to publish. Run './publish.sh publish' to upload to PyPI"
        echo "Or run './publish.sh test' to test upload to Test PyPI first"
        ;;
    *)
        echo "Usage: $0 {build|test|publish|all}"
        exit 1
        ;;
esac