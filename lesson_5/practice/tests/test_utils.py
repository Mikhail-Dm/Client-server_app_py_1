import json
import unittest
import os
import sys
from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR

sys.path.append(os.path.join(os.getcwd(), '..'))
from common.variables import *
from common.utils import get_message, send_message
from common.variables import ACTION, PRESENCE, TIME, USER, ACCOUNT_NAME, RESPONSE, \
    ERROR, DEFAULT_PORT, DEFAULT_IP_ADDRESS, MAX_CONNECTIONS



class TestUtils(unittest.TestCase):
    test_message = {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest'}}
    test_response_dict = {'test_message_dict': 'hello world'}
    test_error_response_dict = ['test_message_list', 'hello world']

    # инициализируем тестовые сокеты для клиента и для сервера
    server_socket = None
    client_socket = None


    def setUp(self) -> None:
        # Создаем тестовый сокет для сервера
        self.server_socket = socket(AF_INET, SOCK_STREAM)
        self.server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.server_socket.bind((DEFAULT_IP_ADDRESS, DEFAULT_PORT))
        self.server_socket.listen(MAX_CONNECTIONS)

        # Создаем тестовый сокет для клиента
        self.client_socket = socket(AF_INET, SOCK_STREAM)
        self.client_socket.connect((DEFAULT_IP_ADDRESS, DEFAULT_PORT))
        self.client, self.client_address = self.server_socket.accept()

    def tearDown(self) -> None:
        # Закрываем созданные сокеты
        self.client.close()
        self.client_socket.close()
        self.server_socket.close()


    def test_get_message_200(self):
        """Корректрая расшифровка коректного словаря"""
        # Отправляем клиенту тестовый ответ о корректной отправке данных
        message = json.dumps(self.test_response_dict)
        self.client.send(message.encode(ENCODING))
        self.client.close()
        # получаем ответ
        response = get_message(self.client_socket)
        # сравниваем отправленный и полученный ответ
        self.assertEqual(self.test_response_dict, response)

    def test_get_message_400(self):
        """Корректрая расшифровка ошибочного словаря"""
        # Отправляем клиенту тестовый ответ об ошибке
        message = json.dumps(self.test_response_dict)
        self.client.send(message.encode(ENCODING))
        self.client.close()
        # получаем ответ
        response = get_message(self.client_socket)
        # сравниваем отправленный и полученный ответ
        self.assertEqual(self.test_response_dict, response)

    def test_get_message_dict(self):
        """Проверяет является ли возвращаемый объект словарем"""
        message = json.dumps(self.test_response_dict)
        self.client.send(message.encode(ENCODING))
        self.client.close()

        self.assertIsInstance(get_message(self.client_socket), dict)

    def test_get_message_not_dict(self):
        """Проверяем возникновение ошибки, если пришедший объект не словарь"""
        # Отправляем клиенту строку, вместо словаря
        message = json.dumps(self.test_error_response_dict)
        self.client.send(message.encode(ENCODING))
        self.client.close()

        self.assertRaises(ValueError, get_message, self.client_socket)


    def test_send_message_client_server(self):
        """Проверяем отправку корректного сообщения"""
        # Отправляем сообщение
        send_message(self.client_socket, self.test_message)
        # Получаем и раскодируем сообщение
        test_response = self.client.recv(MAX_PACKAGE_LENGTH)
        test_response = json.loads(test_response.decode(ENCODING))
        self.client.close()
        # Проверяем соответствие изначального сообщения и прошедшего отправку
        self.assertEqual(self.test_message, test_response)

    def test_send_wrong_message_from_client(self):
        """Проверяем исключение, если на входе не словарь"""
        self.assertRaises(TypeError, send_message, self.client_socket,
                          self.test_error_response_dict)



if __name__ == '__main__':
    unittest.main()
