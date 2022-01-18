import unittest
import sys
import os

sys.path.append(os.path.join(os.getcwd(), '..'))
from server import process_client_message
from common.variables import ACTION, PRESENCE, TIME, USER, ACCOUNT_NAME, RESPONSE, \
    ERROR, DEFAULT_PORT, DEFAULT_IP_ADRESS, MAX_CONNECTIONS



class TestClassServer(unittest.TestCase):
    ok_dict = {RESPONSE: 200}
    err_dict = {
        RESPONSE: 400,
        ERROR: 'Bad Request'
    }


    def setUp(self):
        """Выполнить настройку тестов (если необходимо)"""
        pass

    def tearDown(self):
        """Выполнить завершающие действия (если необходимо)"""
        pass


    def test_process_client_message(self):
        """Тестирование обработки корректных вводных данных"""
        self.assertEqual(process_client_message(
            {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest'}}), self.ok_dict)


    # Тестирование обработки некорректных вводных данных
    def test_process_client_message_incorrect_ACTION(self):
        """Некорректное ACTION"""
        self.assertEqual(process_client_message(
            {ACTION: 'False', TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest'}}), self.err_dict)

    def test_process_client_message_empty_TIME(self):
        """Отсутствие TIME"""
        self.assertEqual(process_client_message(
            {ACTION: PRESENCE, USER: {ACCOUNT_NAME: 'Guest'}}), self.err_dict)

    def test_process_client_message_incorrect_NAME(self):
        """Некорректное ACCOUNT_NAME"""
        self.assertEqual(process_client_message(
            {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Inc_Name'}}), self.err_dict)



if __name__ == '__main__':
    unittest.main()
