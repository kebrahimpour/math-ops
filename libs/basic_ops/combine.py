# /root/math/math-ops/libs/basic_ops/combine.py

from libs.basic_ops.add import add
from libs.basic_ops.subtract import subtract
from libs.basic_ops.multiply import multiply
from libs.basic_ops.divide import divide

def add_then_multiply(first_number, second_number, multiplier):
    """Add two numbers and then multiply the result by a multiplier."""
    sum_result = add(first_number, second_number)
    return multiply(sum_result, multiplier)

def subtract_then_divide(first_number, second_number, divisor):
    """Subtract two numbers and then divide the result by a divisor."""
    difference = subtract(first_number, second_number)
    if divisor == 0:
        raise ValueError("Division by zero is not allowed.")
    return divide(difference, divisor)

def combine_all_operations(first_number, second_number, multiplier, divisor):
    """Combine all operations: add, subtract, multiply, and divide."""
    # Add the numbers
    addition_result = add(first_number, second_number)
    # Subtract the numbers
    subtraction_result = subtract(first_number, second_number)
    # Multiply the addition result by the multiplier
    multiplication_result = multiply(addition_result, multiplier)
    # Divide the subtraction result by the divisor
    if divisor == 0:
        raise ValueError("Division by zero is not allowed.")
    division_result = divide(subtraction_result, divisor)
    
    return addition_result, subtraction_result, multiplication_result, division_result
