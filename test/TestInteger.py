from pynfinity import Integer
from unittest import TestCase, main


class TestInteger(TestCase):
    def test_add(self):

        self.assertEqual(Integer("1") + Integer("2"), Integer("3"))
        self.assertEqual(Integer("123456789101112131415") + Integer("151413121110987654321"),
                         Integer("274869910212099785736"))

    def test_multiply(self):

        self.assertEqual(Integer("30") * Integer("32"), Integer("960"))
        self.assertEqual(Integer("15") * Integer("15"), Integer("225"))
        self.assertEqual(Integer("25") * Integer("25"), Integer("625"))
        self.assertEqual(Integer("321321321") * Integer("123123"),
                         Integer("39562045005483")
        )

    def test_subtract(self):

        self.assertEqual(Integer("100") - Integer("99"), Integer("1"))
        self.assertEqual(Integer("7200000000000000000") - Integer("199999999999"),
                         Integer("7199999800000000001")
        )
        self.assertIsNone(Integer("99") - Integer("100"))
        self.assertIsNone(Integer("77") - Integer("88"))

    def test_divmod(self):

        self.assertEqual(divmod(Integer("99"), Integer("3")), (Integer("33"), Integer("0")))
        self.assertEqual(divmod(Integer("123"), Integer("2")), (Integer("61"), Integer("1")))
        self.assertEqual(divmod(Integer("4444444444444444444444444444444"),
                                Integer("22222222222222222")),
                         (Integer("200000000000000"), Integer("44444444444444"))
        )
        self.assertEqual(divmod(Integer("1"), Integer("0")), (None, None))

if __name__ == '__main__':
    main()
