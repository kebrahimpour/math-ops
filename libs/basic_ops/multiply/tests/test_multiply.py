"""
Tests for the basic multiplication operations module.
"""

from libs.basic_ops.multiply import multiply


def test_multiplication():
    """Test the multiply function."""

    assert multiply(5, 3) == 15