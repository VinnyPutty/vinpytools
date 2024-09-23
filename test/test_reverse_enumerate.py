import unittest

from vinpytools import generator, iterator


class MyTestCase(unittest.TestCase):
    def test_basic_str_list(self):
        original = ["zero", "one", "two"]
        expected = list(reversed(list(enumerate(original))))

        actual = list(generator.reverse_enumerate(original))
        self.assertEqual(actual, expected)

        actual = list(iterator.reverse_enumerate(original))
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
