# /root/math/math-ops/tests/test_combine_operations.py

import unittest
from libs.basic_ops.combine import add_then_multiply, subtract_then_divide, combine_all_operations

class TestCombinedOperations(unittest.TestCase):
    
    def test_add_then_multiply(self):
        # Add 2 + 3 = 5, then multiply by 2 -> 5 * 2 = 10
        self.assertEqual(add_then_multiply(2, 3, 2), 10)
        
    def test_subtract_then_divide(self):
        # Subtract 5 - 3 = 2, then divide by 2 -> 2 / 2 = 1
        self.assertEqual(subtract_then_divide(5, 3, 2), 1)
        
        # Test division by zero (should raise ValueError)
        with self.assertRaises(ValueError):
            subtract_then_divide(5, 3, 0)
    
    def test_combine_all_operations(self):
        # Add 2 + 3 = 5, subtract 5 - 3 = 2, multiply 5 * 2 = 10, divide 2 / 2 = 1
        addition, subtraction, multiplication, division = combine_all_operations(2, 3, 2, 2)
        
        self.assertEqual(addition, 5)
        self.assertEqual(subtraction, 2)
        self.assertEqual(multiplication, 10)
        self.assertEqual(division, 1)
        
        # Test division by zero in combined operations (should raise ValueError)
        with self.assertRaises(ValueError):
            combine_all_operations(5, 3, 2, 0)

if __name__ == "__main__":
    unittest.main()
