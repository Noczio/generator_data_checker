import unittest
from src.check import check_arguments
from resources.exceptions.error import *


class MyTestCase(unittest.TestCase):

    def test_float_are_valid_1(self):
        arguments = ("0.7", "0.1", "3", "5", "10.0")
        key_arguments = {"min": 0, "max": 10, "expected": float}
        are_valid = check_arguments(*arguments, **key_arguments)
        self.assertTrue(all(are_valid))

    def test_float_are_valid_2(self):
        arguments = ("0.7", "0.1", "3", "5", "10.0")
        key_arguments = {"min": 0, "max": 10, "expected": float}
        are_valid = check_arguments(*arguments, **key_arguments)
        self.assertTrue(all(are_valid))

    def test_raises_not_enough_args_error(self):
        with self.assertRaises(NotEnoughArgumentsError):
            arguments = ()
            key_arguments = {"min": 0, "max": 10, "expected": int}
            are_valid = check_arguments(*arguments, **key_arguments)
            self.assertTrue(all(are_valid))

    def test_raises_key_error(self):
        with self.assertRaises(KeyError):
            arguments = ("0.7", "0.1", "3", "5", "10.0")
            key_arguments = {"left_border": 0, "max": 10, "expected": int}
            are_valid = check_arguments(*arguments, **key_arguments)
            self.assertTrue(all(are_valid))


if __name__ == '__main__':
    unittest.main()