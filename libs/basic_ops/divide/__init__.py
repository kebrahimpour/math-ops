"""
Module for basic division operations.
"""

def divide(first_number, second_number):
    """Divide two numbers. Raises an exception if dividing by zero."""
    if second_number == 0:
        raise ValueError("Division by zero is not allowed.")
    return first_number / second_number
