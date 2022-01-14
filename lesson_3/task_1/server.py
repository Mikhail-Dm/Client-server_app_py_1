"""Программа сервера"""

from socket import socket, AF_INET, SOCK_STREAM
import sys
import json
from common.utils import get_message, send_message
from common.variables import ACTION, PRESENCE, TIME, USER, ACCOUNT_NAME, RESPONSE, RESPONDEFAULT_IP_ADRESSSE, ERROR, \
    DEFAULT_PORT, DEFAULT_IP_ADRESS, MAX_CONNECTIONS



def process_client_message(message):
    if ACTION in message and message[ACTION] == PRESENCE and TIME in message and USER in message and \
            message[USER][ACCOUNT_NAME] == 'Guest':
        return {RESPONSE: 200}
    return {
        RESPONDEFAULT_IP_ADRESSSE: 400,
        ERROR: 'Bad Request'
    }


def main():
    try:
        if '-p' in sys.argv:
            listen_port = int(sys.argv[sys.argv.index('-p') + 1])
        else:
            listen_port = DEFAULT_PORT
        if listen_port < 1024 or listen_port > 65535:
            raise ValueError
    except IndexError:
        print('После параметра -\'p\' нужно указать номер порта.')
        sys.exit(1)
    except ValueError:
        print('В качестве порта может быть указано только число в диапазоне от 1024 до 65535.')
        sys.exit(1)

    # Загружаем адрес для прослушки
    try:
        if '-a' in sys.argv:
            listen_address = sys.argv[sys.argv.index('-a') + 1]
        else:
            listen_address = DEFAULT_IP_ADRESS
    except IndexError:
        print('После параметра -\'a\' необходимо указать прослушиваемый адрес.')
        sys.exit(1)


    # Готовим сокет
    transport = socket(AF_INET, SOCK_STREAM)
    transport.bind((listen_address, listen_port))

    # Слушаем порт
    transport.listen(MAX_CONNECTIONS)

    while True:
        try:
            client, client_address = transport.accept()
        except KeyboardInterrupt:
            print('Сервер остановлен вручную.')
            sys.exit(1)
        try:
            message_from_client = get_message(client)
            print(message_from_client)

            response = process_client_message(message_from_client)
            send_message(client, response)
            client.close()
        except (ValueError, json.JSONDecodeError):
            print('!! Некорректное сообщение клиента !!')
            client.close()


if __name__ == '__main__':
    main()
