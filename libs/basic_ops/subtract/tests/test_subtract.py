"""
Tests for the basic subtraction operations module.
"""

from libs.basic_ops.subtract.subtract import subtract


def test_subtraction():
    """Test the subtract function."""
    assert subtract(5, 3) == 2
