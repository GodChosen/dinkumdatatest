import unittest
from app import noneize, sumit


class TestSimple(unittest.TestCase):
    def test_noneizer(self):
        """
        Test it turn anything into None
        """
        self.assertIsNone(noneize('Input'))

    def test_noneizer_2(self):
        """
        Test it turn anything into None
        """
        self.assertIsNone(noneize('Input', 123), msg="Everything turned into None")

    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1]
        self.assertEqual(sumit(*data), 1)

    def test_sum_none(self):
        """
        Test invalid values dont break it
        """
        self.assertEqual(sumit(None), 0)

    def test_sum_zero(self):
        """
        Test adding zeroes
        """
        self.assertEqual(sumit(*[0, 0, 0]), 0)


if __name__ == '__main__':
    print("Testing")
    unittest.main()
    print("Tests finished")
