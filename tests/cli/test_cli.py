"""
Module: CLI Tests

This module contains unit tests and integration tests for the CLI.

### Tasks for Students:
1. Write tests for the `add_numbers` function.
2. Write integration tests to simulate running the CLI from the command line.

Tools:
- Use `pytest` to write and execute tests.
"""
import pytest  # pylint: disable=import-error
from src.cli import calculate


def test_addition():
    """Test the add_numbers function."""

    assert calculate("2 + 2") == 4


def test_subtraction():
    """Test the subtract_numbers function."""

    assert calculate("5 - 3") == 2


def test_multiplication_not_implemented():
    """Test the multiply_numbers function."""

    with pytest.raises(NotImplementedError):
        calculate("3 * 3")


def test_division_not_implemented():
    """Test the divide_numbers function."""

    with pytest.raises(NotImplementedError):
        calculate("10 / 2")


def test_unsupported_operation():
    """Test an unsupported operation."""

    assert calculate("2 ^ 2") == "Unsupported operation"


def test_invalid_expression():
    """Test an invalid expression."""

    assert "Error" in calculate("2 +")


def test_non_numeric_input():
    """Test non-numeric input."""

    assert "Error" in calculate("two + two")
