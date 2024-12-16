import unittest
from libs.basic_ops.divide import divide

class TestBasicOps(unittest.TestCase):
    

    def test_divide(self):
        self.assertEqual(divide(6, 3), 2)
        self.assertRaises(ZeroDivisionError, divide, 5, 0)

if __name__ == '__main__':
    unittest.main()
