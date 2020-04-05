import unittest
import suma

class TestMyModule(unittest.TestCase):
    def test_total(self):
        self.assertEqual(suma.total(2,2),4)

if __name__ == '__main__':
    unittest.main()