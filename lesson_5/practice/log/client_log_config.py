# logging - стандартный модуль для организации логирования
import logging


def handler_client_func(message_log, dir_way):
    # Создаем объект-логгер с именем app.main_client:
    logger = logging.getLogger('app.client')

    # Создаем объект форматирования:
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(module)s - %(message)s ")

    # Создаем файловый обработчик логирования (можно задать кодировку):
    file_handler = logging.FileHandler(dir_way, encoding='utf-8')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    # Добавляем в логгер новый обработчик событий и устанавливаем уровень логирования
    logger.addHandler(file_handler)
    logger.setLevel(logging.DEBUG)
    logger.debug(message_log)

def main_client():
    handler_client_func('Start test client', 'app.main.log')


if __name__ == '__main__':
    main_client()
