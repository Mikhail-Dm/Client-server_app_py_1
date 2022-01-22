# logging - стандартный модуль для организации логирования
import logging.handlers



# Создаем объект форматирования:
FORMATTER = logging.Formatter("%(asctime)s - %(levelname)s - %(module)s - %(message)s ")

# Создаем файловый обработчик логирования (можно задать кодировку):
FILE_HANDLER = logging.FileHandler('log/client_log/app.client.log')
FILE_HANDLER.setFormatter(FORMATTER)
FILE_HANDLER.setLevel(logging.DEBUG)

# Создаем объект-логгер с именем app.server:
LOGGER_C = logging.getLogger('app.client')
# Добавляем в логгер новый обработчик событий и устанавливаем уровень логирования
LOGGER_C.addHandler(FILE_HANDLER)
LOGGER_C.setLevel(logging.DEBUG)


if __name__ == '__main__':
    STREAM_HANDLER = logging.StreamHandler()
    STREAM_HANDLER.setFormatter(FORMATTER)
    STREAM_HANDLER.setLevel(logging.DEBUG)
    LOGGER_C.addHandler(STREAM_HANDLER)
    LOGGER_C.debug('message')

    # LOGGER_C.critical('Критическая ошибка')
    # LOGGER_C.error('Ошибка')
    # LOGGER_C.debug('Отладочная информация')
    # LOGGER_C.info('Информационное сообщение')
