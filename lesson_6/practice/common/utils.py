import inspect
import json

from .variables import *
from functools import wraps
from practice.log.client_log.client_log_config import *
from practice.log.server_log.server_log_config import *



def get_message(client):
    """
    Принимает сообщение, декодирует, конвертирует в словарь
    :param client:
    :return response:
    """

    encoded_response = client.recv(MAX_PACKAGE_LENGTH)
    if isinstance(encoded_response, bytes):
        json_response = encoded_response.decode(ENCODING)
        response = json.loads(json_response)
        if isinstance(response, dict):
            return response
        raise ValueError
    raise ValueError


def send_message(sock, message):
    """
    Принимает словарь и отправляет его
    :param sock:
    :param message:
    :return:
    """

    if not isinstance(message, dict):
        raise TypeError
    json_message = json.dumps(message)
    encoded_message = json_message.encode('utf-8')
    sock.send(encoded_message)


def log(func):
    @wraps(func)
    def call(*args, **kwargs):
        outer_func = inspect.stack()[1][3]
        LOGGER_S.debug(f'Функция "{func.__name__}" вызвана функцией "{outer_func}"')
        LOGGER_C.debug(f'Функция "{func.__name__}" вызвана функцией "{outer_func}"')
        return func(*args, **kwargs)
    return call
