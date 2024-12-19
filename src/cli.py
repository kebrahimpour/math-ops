"""
Module: Command Line Interface (CLI)

This module provides a CLI for performing basic mathematical operations,
starting with addition.

### Tasks for Students:
1. Implement the `add_numbers` function to add two numbers.
2. Use the `argparse` library to take input from the user via the command line.
3. Display the result to the user.

Example Usage:
    $ python src/cli.py 2 3
    The result of adding 2 and 3 is: 5
"""
import argparse
import operator


def calculate(expression):
    """Calculate the result of a mathematical expression."""

    try:
        # Split the expression into components
        left, operation, right = expression.split()
        left = float(left)
        right = float(right)

        # Define supported operations
        operations = {
            "+": operator.add,
            "-": operator.sub,
            "*": "not_implemented",
            "/": "not_implemented",
        }

        # Perform the operation
        if operation in operations:
            if operations[operation] == "not_implemented":
                raise NotImplementedError(
                    f"The operation '{operation}' is not implemented yet."
                )
            result = operations[operation](left, right)
            return result
        return "Unsupported operation"

    except Exception as exception:
        return f"Error: {exception}"


def main():
    """Parse command-line arguments and calculate the result."""

    parser = argparse.ArgumentParser(description="Simple CLI calculator")
    parser.add_argument(
        "expression",
        type=str,
        help="Mathematical expression to evaluate (e.g., '2 + 2')",
    )
    args = parser.parse_args()

    result = calculate(args.expression)
    print(f"Result: {result}")


if __name__ == "__main__":
    main()
