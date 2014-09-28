import pynfinity
import unittest


class TestInteger(unittest.TestCase):
    def test_add(self):

        self.assertEqual(pynfinity.Integer("1") + pynfinity.Integer("2"), pynfinity.Integer("3"))

    def test_multiply(self):

        self.assertEqual(pynfinity.Integer("30") * pynfinity.Integer("32"), pynfinity.Integer("960"))
        self.assertEqual(pynfinity.Integer("15") * pynfinity.Integer("15"), pynfinity.Integer("225"))
        self.assertEqual(pynfinity.Integer("25") * pynfinity.Integer("25"), pynfinity.Integer("625"))

if __name__ == '__main__':
    unittest.main()
