import unittest

from main import add_numbers


class MyTestCase(unittest.TestCase):
    def test_add_numbers(self):
        result = add_numbers([1, 1,])
        self.assertEqual(result, 2)


if __name__ == '__main__':
    unittest.main()
