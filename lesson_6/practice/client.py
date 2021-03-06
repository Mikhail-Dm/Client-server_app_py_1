"""Программа клиента"""

import json
import sys
import time

from socket import socket, AF_INET, SOCK_STREAM
from common.variables import ACTION, PRESENCE, TIME, USER, ACCOUNT_NAME, RESPONSE, ERROR, \
    DEFAULT_IP_ADDRESS, DEFAULT_PORT
from common.utils import get_message, send_message
from log.client_log.client_log_config import *
from common.utils import log



@log
def create_presence(account_name='Guest'):
    """
    Функция генерирует запрос о присутствии клиента
    :param account_name:
    :return:
    """
    LOGGER_C.debug('Генерируем запрос о присутствии клиента.')
    out = {
        ACTION: PRESENCE,
        TIME: time.ctime(time.time()),
        USER: {
            ACCOUNT_NAME: account_name
        }
    }
    return out

@log
def process_ans(message):
    """
    Функция разбирает ответ сервера
    :param message:
    :return:
    """
    LOGGER_C.debug('Разбираем сообщение от сервера.')
    if RESPONSE in message:
        if message[RESPONSE] == 200:
            return '200: OK'
        return f'400: {message[ERROR]}'
    raise ValueError

@log
def main():
    """
    Загружает параметры командной строки
    :return:
    """
    LOGGER_C.debug('Старт клиента')
    try:
        server_address = sys.argv[1]  # server_address: '127.0.0.1'
        server_port = int(sys.argv[2])  # server_port: 7777
        if server_port < 1024 or server_port > 65535:
            raise ValueError
    except ValueError:
        LOGGER_C.debug('В качестве порта может быть указано только число в диапазоне от 1024 до 65535')
        sys.exit(1)
    except IndexError:
        LOGGER_C.debug(f'Подключение к порту и IP-адресу по умолчанию. PORT: {DEFAULT_PORT}, IP: {DEFAULT_IP_ADDRESS}.')
        server_address = DEFAULT_IP_ADDRESS
        server_port = DEFAULT_PORT

    # Инициализация сокета и обмен
    LOGGER_C.debug('Инициализация сокета и обмен')
    transport = socket(AF_INET, SOCK_STREAM)
    try:
        LOGGER_C.debug('Попытка подключения к серверу')
        transport.connect((server_address, server_port))
    except ConnectionRefusedError:
        print('!! Сервер не запущен !!')
        sys.exit(1)

    message_to_server = create_presence()
    send_message(transport, message_to_server)
    LOGGER_C.debug(f'Успешная попытка подключения к серверу, отправляем сообщение: {message_to_server}')
    try:
        LOGGER_C.debug('Попытка получения ответа от сервера.')
        answer = process_ans(get_message(transport))
        LOGGER_C.debug(f'Успешная попытка, ответ получен: {answer}.')
    except (ValueError, json.JSONDecodeError):
        LOGGER_C.debug('Не удалось декодировать сообщение сервера.')


if __name__ == '__main__':
    main()
