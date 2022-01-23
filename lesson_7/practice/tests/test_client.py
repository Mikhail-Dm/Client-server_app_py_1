import unittest
import sys
import os

sys.path.append(os.path.join(os.getcwd(), '..'))
from client import create_presence, process_ans
from common.variables import ACTION, PRESENCE, TIME, USER, ACCOUNT_NAME, RESPONSE, ERROR, \
    DEFAULT_IP_ADRESS, DEFAULT_PORT



class TestClassClient(unittest.TestCase):

    def setUp(self):
        """Выполнить настройку тестов (если необходимо)"""
        pass

    def tearDown(self):
        """Выполнить завершающие действия (если необходимо)"""
        pass

    def test_create_presence(self):
        """Тестирование обработки данных"""
        test_list = create_presence()
        test_list[TIME] = 1.1
        self.assertEqual(test_list, {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest'}})

    def test_create_presence_incorrect_params(self):
        """Тестирование обработки ввода некорректных данных"""
        test_list = create_presence()
        # test_list[TIME] = 1.1
        self.assertNotEqual(test_list, {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Inc_Name'}})

    def test_process_ans_200(self):
        """Тестирование ответа сервера 200"""
        self.assertEqual(process_ans({RESPONSE: 200}), '200: OK')

    def test_process_ans_400(self):
        """Тестирование ответа сервера 400, неверный ответ сервера"""
        self.assertEqual(process_ans({RESPONSE: 400, ERROR: 'error 400'}), '400: error 400')

    def test_process_ans_400_no_response(self):
        """Тестирование исключения ValueError, когда нет RESPONSE"""
        self.assertRaises(ValueError, process_ans, '400: error 400')


if __name__ == '__main__':
    unittest.main()
