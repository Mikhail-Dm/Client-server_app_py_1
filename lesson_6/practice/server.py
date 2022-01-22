"""Программа сервера"""

from socket import socket, AF_INET, SOCK_STREAM
import sys
import json

from common.utils import get_message, send_message
from common.variables import ACTION, PRESENCE, TIME, USER, ACCOUNT_NAME, RESPONSE, ERROR, DEFAULT_PORT, \
    DEFAULT_IP_ADDRESS, MAX_CONNECTIONS
from log.server_log.server_log_config import *
from common.utils import log



@log
def process_client_message(message):
    LOGGER_S.debug('Проверяем корректность сообщения.')
    if ACTION in message and message[ACTION] == PRESENCE and TIME in message and USER in message and \
            message[USER][ACCOUNT_NAME] == 'Guest':
        LOGGER_S.debug('Корректное сообщение.')
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
    LOGGER_S.debug('Запуск сервера')
    try:
        if '-p' in sys.argv:
            listen_port = int(sys.argv[sys.argv.index('-p') + 1])
            LOGGER_S.debug(f'Подключение к указанному порту: {listen_port}.')
        else:
            listen_port = DEFAULT_PORT
            LOGGER_S.debug('Подключение к порту по-умолчанию.')
        if listen_port < 1024 or listen_port > 65535:
            raise ValueError
    except IndexError:
        LOGGER_S.debug('После параметра -\'p\' нужно указать номер порта')
        sys.exit(1)
    except ValueError:
        LOGGER_S.debug('В качестве порта может быть указано только число в диапазоне от 1024 до 65535.')
        sys.exit(1)

    # Загружаем адрес для прослушки
    LOGGER_S.debug('Загружаем адрес для прослушки.')
    try:
        if '-a' in sys.argv:
            listen_address = sys.argv[sys.argv.index('-a') + 1]
            LOGGER_S.debug(f'Подключение к указанному IP-адресу: {listen_address}.')
        else:
            listen_address = DEFAULT_IP_ADDRESS
            LOGGER_S.debug(f'Подключение к IP-адресу по умолчанию: {listen_address}.')
    except IndexError:
        LOGGER_S.debug('После параметра -\'a\' необходимо указать прослушиваемый адрес.')
        sys.exit(1)

    # Готовим сокет
    LOGGER_S.debug('Готовим сокет.')
    transport = socket(AF_INET, SOCK_STREAM)
    try:
        transport.bind((listen_address, listen_port))
    except OSError:
        print('!! Порт занят !!')
        sys.exit(1)

    # Слушаем порт
    LOGGER_S.debug('Слушаем порт.')
    transport.listen(MAX_CONNECTIONS)

    while True:
        try:
            client, client_address = transport.accept()
            LOGGER_S.debug('Принимаем соединение.')
        except KeyboardInterrupt:
            sys.exit(1)

        try:
            LOGGER_S.debug('Попытка получения сообщения от клиента.')
            message_from_client = get_message(client)
            LOGGER_S.debug(f'Принимаем сообщение: {message_from_client}')
            response = process_client_message(message_from_client)
            send_message(client, response)
            client.close()
            LOGGER_S.debug('Успешная попытка получения сообщения от клиента.')
        except (ValueError, json.JSONDecodeError):
            LOGGER_S.debug(f'Ошибка: {RESPONSE}, "{ERROR}"')
            client.close()


if __name__ == '__main__':
    main()
