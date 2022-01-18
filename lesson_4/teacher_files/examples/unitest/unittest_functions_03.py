"""assertEqual"""
import sys

import my_file
import unittest
from unittest.mock import patch


def sum_of_squares(i, j):
    """Сумма квадратов"""
    return i ** 2 + j ** 2


def val_compare(val_1, val_2):
    """Сравнение значений"""
    return val_1 > val_2


class Plane:
    """class"""
    pass


class Car:
    """class"""
    pass


def is_compare(val_1, val_2):
    return val_1 is val_2


def is_none(val_1):
    val_2 = val_1
    return val_2


class TestSumKV(unittest.TestCase):
    """создаем тестовый случай"""

    def test_equal(self):
        """создаем сам тест"""

        # используем функцию assertEqual
        self.assertEqual(sum_of_squares(2, 3), 13)

    def test_not_equal(self):
        """используем функцию assertNotEqual"""
        self.assertNotEqual(sum_of_squares(2, 3), 10)

    def test_true(self):
        """используем функцию assertTrue"""
        self.assertTrue(val_compare(10, 3), True)

    def test_false(self):
        """используем функцию assertTrue"""
        self.assertFalse(val_compare(10, 30), False)

    def test_is(self):
        """используем функцию assertIs"""
        self.assertIs(is_compare(Plane(), Plane()), False)

    def test_is_not(self):
        """используем функцию assertIsNot"""
        self.assertIsNot(is_compare(Plane(), Plane()), True)

    def test_is_none(self):
        """используем функцию assertIsNone"""
        self.assertIsNone(is_none(None), True)

    def test_is_not_none(self):
        """используем функцию assertIsNotNone"""
        self.assertIsNotNone(is_none("string"), True)

    def test_in(self):
        """используем функцию assertIn"""
        self.assertIn(1, [1, 2, 3])

    def test_not_in(self):
        """используем функцию assertNotIn"""
        self.assertNotIn(4, [1, 2, 3])

    def test_isinstance(self):
        """используем функцию assertIsInstance"""
        self.assertIsInstance(Plane(), Plane)

    def test_not_isinstance(self):
        """используем функцию assertNotIsInstance"""
        self.assertNotIsInstance(Plane(), Car)

    def test_raises_with_with(self):
        """используем функцию assertRaises"""
        with self.assertRaises(ZeroDivisionError):
            1 // 0

    def test_raises_without_with(self):
        """используем функцию assertRaises"""
        division_by_zero = lambda x: x / 0
        self.assertRaises(ZeroDivisionError, division_by_zero, 5)

    @patch.object(sys, 'argv', ['my_file.py', '-p'])   # sys.argv = ['my_file.py', '-p']
    def test_with_mock_patch_function_my_func_false_var1(self):
        """
        Используем функцию assertRaises и unittest.mock.patch
        для проверки числа аргументов, переданных при запуске файла
        """
        self.assertRaises(IndexError, my_file.my_func)

    def test_with_mock_patch_function_my_func_false_var2(self):
        """
        Используем функцию assertRaises и unittest.mock.patch
        для проверки числа аргументов, переданных при запуске файла
        """
        file_and_args = ['my_file.py', '-p']
        with patch.object(sys, 'argv', file_and_args):
            self.assertRaises(IndexError, my_file.my_func)

    @patch.object(sys, 'argv', ['my_file.py', '-p', 7777])
    def test_with_mock_patch_function_my_func_true(self):
        """
        Используем функцию assertRaises и unittest.mock.patch
        для проверки числа аргументов, переданных при запуске файла
        """
        self.assertEqual(None, my_file.my_func())

    def test_with_mock_patch_function_get_port_number_false(self):
        """
        Используем функцию assertRaises и unittest.mock.patch
        для проверки числа аргументов, переданных при запуске файла
        """
        file_and_args = ['my_file.py', '-p']
        with patch.object(sys, 'argv', file_and_args):
            self.assertRaises(IndexError, my_file.get_port_number)

    def test_with_mock_patch_function_get_port_number_true(self):
        """
        Используем функцию assertRaises и unittest.mock.patch
        для проверки числа аргументов, переданных при запуске файла
        """
        file_and_args = ['my_file.py', '-p', 7777]
        with patch.object(sys, 'argv', file_and_args):
            self.assertEqual(7777, my_file.get_port_number())


if __name__ == '__main__':
    unittest.main()
