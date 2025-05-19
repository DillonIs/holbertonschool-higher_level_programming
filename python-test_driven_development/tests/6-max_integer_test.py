#!/usr/bin/python3
"""Defines a class as TestMaxInteger for max_integer([...])"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    Defines test cases for the max_integer function
    """
    def test_positive_integers(self):
        test_list1 = [1, 2, 3, 4]
        test_list2 = [4, 1, 2, 3]
        test_list3 = [1, 2, 4, 2, 3]

        self.assertEqual(max_integer(test_list1), 4)
        self.assertEqual(max_integer(test_list2), 4)
        self.assertEqual(max_integer(test_list3), 4)

    def test_negative_integers(self):
        test_list1 = [-91, -31, -4, -2]
        test_list2 = [-2, -91, -31, -4]
        test_list3 = [-91, -123, -2, -31, -4]

        self.assertEqual(max_integer(test_list1), -2)
        self.assertEqual(max_integer(test_list2), -2)
        self.assertEqual(max_integer(test_list3), -2)

    def pos_neg_ints(self):
        test_list = [-9, -14, 23, 98, 0, -9, -100, -1]
        self.assertEqual(max_integer(test_list), 98)

    def empty_test(self):
        test_list = []
        self.assertEqual(max_integer(test_list), None)

    def solo_arg(self):
        test_list = [9]
        self.assertEqual(max_integer(test_list), 9)

    def no_arg(self):
        with self.assertRaises(TypeError):
            max_integer(None)

    def list_has_none(self):
        with self.assertRaises(TypeError):
            test_list = [1, 2, 3, 4, None]
            max_integer(test_list)

    def list_None(self):
        test_list = [None]
        self.assertIsNone(max_integer(test_list), None)

    def list_int_string(self):
        test_list = [1, 2, 3, 4, "2"]
        with self.assertRaises(TypeError):
            max_integer(test_list)

    def list_int_as_string(self):
        test_list = ["1234"]
        self.assertEqual(max_integer(test_list), "1234")

    def one_int_repeat(self):
        test_listpos = [9, 9, 9, 9]
        test_listneg = [-20, -20, -20, -20]
        self.assertEqual(max_integer(test_listpos), 9)
        self.assertEqual(max_integer(test_listneg), -20)

    def if_zero(self):
        test_list = [0]
        self.assertEqual(max_integer(test_list), 0)

    def if_dict(self):
        test_list = [{'key1': 1}, {'key2' : 9}]
        with self.assertRaises(TypeError):
            max_integer(test_list)

    def if_list_in_list(self):
        test_list = [1, 9, 7, [7, 9, 1]]
        with self.assertRaises(TypeError):
            max_integer(test_list)

    def if_tuple_list(self):
        test_list = [1, 9, 7, (9, 7, 1)]
        with self.assertRaises(TypeError):
            max_integer(test_list)

    def if_set_list(self):
        test_list = [1, 9, 7, {7, 9, 1}]
        with self.assertRaises(TypeError):
            max_integer(test_list)

    def character_list(self):
        test_list = ['a', 'c', 'd', 'v']
        self.assertEqual(max_integer(test_list), 'v')
