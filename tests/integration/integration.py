"""
Module to combine all basic operations.
"""

from libs.basic_ops.add import add
from libs.basic_ops.subtract import subtract
from libs.basic_ops.multiply import multiply
from libs.basic_ops.divide import divide

def combine_operations(a, b, c, d):
    """Perform a combination of operations."""
    return add(a, b), subtract(a, b), multiply(a, c), divide(a, d)
