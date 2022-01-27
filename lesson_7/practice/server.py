"""Программа сервера"""

from socket import socket, AF_INET, SOCK_STREAM
import json
import sys
import logging

from common.utils import get_message, send_message
from common.variables import ACTION, PRESENCE, TIME, USER, ACCOUNT_NAME, RESPONSE, ERROR, DEFAULT_PORT, \
    DEFAULT_IP_ADDRESS, MAX_CONNECTIONS
import log.server_log.server_log_config
from decos import log



# Инициализация серверного логера
LOGER = logging.getLogger('server')

@log
def process_client_message(message):
    LOGER.debug('Проверяем корректность сообщения.')
    if ACTION in message and message[ACTION] == PRESENCE and TIME in message and USER in message and \
            message[USER][ACCOUNT_NAME] == 'Guest':
        LOGER.debug('Корректное сообщение.')
        return {RESPONSE: 200}
    return {
        RESPONSE: 400,
        ERROR: 'Bad Request'
    }

@log
def main():
    """
    Функция запускает сервер
    :return:
    """
    LOGER.debug('Запуск сервера')
    try:
        if '-p' in sys.argv:
            listen_port = int(sys.argv[sys.argv.index('-p') + 1])
            LOGER.debug(f'Подключение к указанному порту: {listen_port}.')
        else:
            listen_port = DEFAULT_PORT
            LOGER.debug('Подключение к порту по-умолчанию.')
        if listen_port < 1024 or listen_port > 65535:
            raise ValueError
    except IndexError:
        LOGER.debug('После параметра -\'p\' нужно указать номер порта')
        sys.exit(1)
    except ValueError:
        LOGER.debug('В качестве порта может быть указано только число в диапазоне от 1024 до 65535.')
        sys.exit(1)

    # Загружаем адрес для прослушки
    LOGER.debug('Загружаем адрес для прослушки.')
    try:
        if '-a' in sys.argv:
            listen_address = sys.argv[sys.argv.index('-a') + 1]
            LOGER.debug(f'Подключение к указанному IP-адресу: {listen_address}.')
        else:
            listen_address = DEFAULT_IP_ADDRESS
            LOGER.debug(f'Подключение к IP-адресу по умолчанию: {listen_address}.')
    except IndexError:
        LOGER.debug('После параметра -\'a\' необходимо указать прослушиваемый адрес.')
        sys.exit(1)

    # Готовим сокет
    LOGER.debug('Готовим сокет.')
    transport = socket(AF_INET, SOCK_STREAM)
    try:
        transport.bind((listen_address, listen_port))
    except OSError:
        print('!! Порт занят !!')
        sys.exit(1)

    # Слушаем порт
    LOGER.debug('Слушаем порт.')
    transport.listen(MAX_CONNECTIONS)

    while True:
        try:
            client, client_address = transport.accept()
            LOGER.debug('Принимаем соединение.')
        except KeyboardInterrupt:
            sys.exit(1)

        try:
            LOGER.debug('Попытка получения сообщения от клиента.')
            message_from_client = get_message(client)
            LOGER.debug(f'Принимаем сообщение: {message_from_client}')
            response = process_client_message(message_from_client)
            send_message(client, response)
            client.close()
            LOGER.debug('Успешная попытка получения сообщения от клиента.')
        except (ValueError, json.JSONDecodeError):
            LOGER.debug(f'Ошибка: {RESPONSE}, "{ERROR}"')
            client.close()


if __name__ == '__main__':
    main()
