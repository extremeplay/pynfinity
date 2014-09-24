import pynfinity
import unittest


class TestInteger(unittest.TestCase):
    def test_something(self):
        a = pynfinity.Integer("1")
        b = pynfinity.Integer("2")
        c = a + b
        self.assertEqual(str(c), "3")

if __name__ == '__main__':
    unittest.main()
