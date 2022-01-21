# logging - стандартный модуль для организации логирования
import logging
from logging.handlers import TimedRotatingFileHandler


def handler_server_func(message_log, dir_way):
    # Создаем объект-логгер с именем app.main:
    logger = logging.getLogger('app_test.main')

    # Создаем объект форматирования:
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(module)s - %(message)s ")

    # Создаем файловый обработчик логирования (можно задать кодировку):
    # file_handler = logging.FileHandler(dir_way, encoding='utf-8')
    # file_handler.setLevel(logging.DEBUG)
    # file_handler.setFormatter(formatter)

    handler = logging.handlers.TimedRotatingFileHandler(
        filename=dir_way,
        when='H',
        interval=24,
        encoding='utf-8',
    )
    handler.suffix = '%Y-%m-%d'
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(formatter)

    # Добавляем в логгер новый обработчик событий и устанавливаем уровень логирования
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    logger.debug(message_log)



def main():
    handler_server_func('Start test_test server', 'app.main.log')


if __name__ == '__main__':
    main()
