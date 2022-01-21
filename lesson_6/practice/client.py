"""Программа клиента"""

import json
import sys
import time

from socket import socket, AF_INET, SOCK_STREAM
from common.variables import ACTION, PRESENCE, TIME, USER, ACCOUNT_NAME, RESPONSE, ERROR, \
    DEFAULT_IP_ADDRESS, DEFAULT_PORT
from common.utils import get_message, send_message
from log import client_log_config



def create_presence(account_name='Guest'):
    """
    Функция генерирует запрос о присутствии клиента
    :param account_name:
    :return:
    """
    out = {
        ACTION: PRESENCE,
        TIME: time.ctime(time.time()),
        USER: {
            ACCOUNT_NAME: account_name
        }
    }
    return out


def process_ans(message):
    """
    Функция разбирает ответ сервера
    :param message:
    :return:
    """
    if RESPONSE in message:
        if message[RESPONSE] == 200:
            return '200: OK'
        return f'400: {message[ERROR]}'
    raise ValueError


def main():
    """
    Загружает параметры командной строки
    :return:
    """
    dir_way = 'log/app.main.log'
    try:
        server_address = sys.argv[1]  # server_address: '127.0.0.1'
        server_port = int(sys.argv[2])  # server_port: 7777
        if server_port < 1024 or server_port > 65535:
            raise ValueError
    except ValueError:
        client_log_config.handler_client_func(
            'В качестве порта может быть указано только число в диапазоне от 1024 до 65535',
            dir_way
        )
        sys.exit(1)
    except IndexError:
        server_address = DEFAULT_IP_ADDRESS
        server_port = DEFAULT_PORT

    # Инициализация сокета и обмен
    transport = socket(AF_INET, SOCK_STREAM)
    try:
        transport.connect((server_address, server_port))
    except ConnectionRefusedError:
        print('!! Сервер не запущен !!')
        sys.exit(1)
    message_to_server = create_presence()
    send_message(transport, message_to_server)
    try:
        answer = process_ans(get_message(transport))
        client_log_config.handler_client_func(
            answer,
            dir_way
        )
    except (ValueError, json.JSONDecodeError):
        client_log_config.handler_client_func(
            'Не удалось декодировать сообщение сервера.',
            dir_way
        )


if __name__ == '__main__':
    main()
