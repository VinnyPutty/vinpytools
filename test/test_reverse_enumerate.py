import unittest

from vinpytools import reverse_enumerate


class MyTestCase(unittest.TestCase):
    def test_basic_str_list(self):
        actual = list(reverse_enumerate(['zero', 'one', 'two']))
        expected = [(2, 'two'), (1, 'one'), (0, 'zero')]
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
