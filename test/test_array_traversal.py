import unittest

from vinpytools import array_traversal


class Test(unittest.TestCase):
    def test_array_traversal(self):
        self.fail()

    def test_basic_array_traversal(self):
        array_traversal([0, 0], [[0, 0], [0, 0]])
        self.fail()

    def test_axis_length_calculation(self):
        # Passes
        input_array = [[[[[1]] * 2] * 3] * 4] * 5
        array_traversal([0, 0, 0, 0, 0], input_array)



if __name__ == '__main__':
    unittest.main()
