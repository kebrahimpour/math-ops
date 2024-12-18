from libs.basic_ops.combine import combine_operations

def test_combine_operations():
    addition, subtraction, multiplication, division = combine_operations(10, 2, 3, 2)
    assert addition == 12
    assert subtraction == 8
    assert multiplication == 30
    assert division == 5


### Tasks for Students:
1. Write integration tests to verify that the CLI interacts correctly
   with the `add` function in `libs/basic_ops/add`.
2. Test edge cases and error scenarios.
"""

from libs.basic_ops.add.add import add
from libs.basic_ops.subtract.subtract import subtract


def test_addition_subtraction():
    """Test the add + subtract function."""

    x_add = add(4, 2)
    y_substract = subtract(x_add, 3)
    assert y_substract == 3
 main
