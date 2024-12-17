
import unittest
from libs.basic_ops.subtract import subtract

class TestBasicOps(unittest.TestCase):
    

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)

if __name__ == '__main__':
    unittest.main()