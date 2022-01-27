import logging
import sys
import practice.log.client_log.client_log_config
import practice.log.server_log.server_log_config



if sys.argv[0].find('client') == -1:
    LOGER = logging.getLogger('server')
else:
    LOGER = logging.getLogger('client')


def log(func):
    """Функция-декоратор"""
    def log_saver(*args, **kwargs):
        outer_func = func(*args, **kwargs)
        LOGER.debug(f'Была вызвана функция "{func.__name__}" из модуля "{func.__module__}"')
        return outer_func
    return log_saver
