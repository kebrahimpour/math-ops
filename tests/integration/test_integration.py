import unittest
from libs.basic_ops.combine import combine_operations

class TestIntegrationOperations(unittest.TestCase):
    def test_combine_operations(self):
        addition, subtraction, multiplication, division = combine_operations(10, 2, 3, 2)
        self.assertEqual(addition, 12)
        self.assertEqual(subtraction, 8)
        self.assertEqual(multiplication, 30)
        self.assertEqual(division, 5)

if __name__ == "__main__":
    unittest.main()
