import unittest
from libs.basic_ops.multiply import multiply

class TestBasicOps(unittest.TestCase):

    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)

    

if __name__ == '__main__':
    unittest.main()
