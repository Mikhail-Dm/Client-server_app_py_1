"""Программа сервера"""

from socket import socket, AF_INET, SOCK_STREAM
import sys
import json

from common.utils import get_message, send_message
from common.variables import ACTION, PRESENCE, TIME, USER, ACCOUNT_NAME, RESPONSE, \
    ERROR, DEFAULT_PORT, DEFAULT_IP_ADDRESS, MAX_CONNECTIONS
from log import server_log_config



def process_client_message(message):
    if ACTION in message and message[ACTION] == PRESENCE and TIME in message and USER in message and \
            message[USER][ACCOUNT_NAME] == 'Guest':
        return {RESPONSE: 200}
    return {
        RESPONSE: 400,
        ERROR: 'Bad Request'
    }


def main():
    """
    Функция запускает сервер
    :return:
    """
    dir_way = 'log/app.main.log'
    try:
        if '-p' in sys.argv:
            listen_port = int(sys.argv[sys.argv.index('-p') + 1])
        else:
            listen_port = DEFAULT_PORT
        if listen_port < 1024 or listen_port > 65535:
            raise ValueError
    except IndexError:
        server_log_config.handler_server_func(
            'После параметра -\'p\' нужно указать номер порта',
            dir_way
        )
        sys.exit(1)
    except ValueError:
        server_log_config.handler_server_func(
            'В качестве порта может быть указано только число в диапазоне от 1024 до 65535',
            dir_way
        )
        sys.exit(1)

    # Загружаем адрес для прослушки
    try:
        if '-a' in sys.argv:
            listen_address = sys.argv[sys.argv.index('-a') + 1]
        else:
            listen_address = DEFAULT_IP_ADDRESS
    except IndexError:
        server_log_config.handler_server_func(
            'После параметра -\'a\' необходимо указать прослушиваемый адрес',
            dir_way
        )
        sys.exit(1)


    # Готовим сокет
    transport = socket(AF_INET, SOCK_STREAM)
    try:
        transport.bind((listen_address, listen_port))
    except OSError:
        print('!! Порт занят !!')
        sys.exit(1)
    # Слушаем порт
    transport.listen(MAX_CONNECTIONS)

    while True:
        try:
            client, client_address = transport.accept()
        except KeyboardInterrupt:
            sys.exit(1)
        try:
            message_from_client = get_message(client)
            server_log_config.handler_server_func(
                message_from_client,
                dir_way
            )
            response = process_client_message(message_from_client)
            send_message(client, response)
            client.close()
        except (ValueError, json.JSONDecodeError):
            server_log_config.handler_server_func(
                '!! Некорректное сообщение клиента !!',
                dir_way
            )
            client.close()


if __name__ == '__main__':
    main()
