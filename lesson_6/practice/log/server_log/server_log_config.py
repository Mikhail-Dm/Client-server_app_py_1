# logging - стандартный модуль для организации логирования
import logging.handlers



# Создаем объект форматирования:
FORMATTER = logging.Formatter("%(asctime)s - %(levelname)s - %(module)s - %(message)s ")

# Создаем файловый обработчик логирования (можно задать кодировку):
HANDLER = logging.handlers.TimedRotatingFileHandler(filename='log/server_log/app.server.log', when='H', interval=24,
                                                    encoding='utf-8')
HANDLER.suffix = '%Y-%m-%d'
HANDLER.setFormatter(FORMATTER)

# Создаем объект-логгер с именем app.server:
LOGGER_S = logging.getLogger('app.server')
# Добавляем в логгер новый обработчик событий и устанавливаем уровень логирования
LOGGER_S.addHandler(HANDLER)
LOGGER_S.setLevel(logging.DEBUG)


if __name__ == '__main__':
    STREAM_HANDLER = logging.StreamHandler()
    STREAM_HANDLER.setFormatter(FORMATTER)
    STREAM_HANDLER.setLevel(logging.DEBUG)
    LOGGER_S.addHandler(STREAM_HANDLER)
    LOGGER_S.debug('message')

    # LOGGER_S.critical('Критическая ошибка')
    # LOGGER_S.error('Ошибка')
    # LOGGER_S.debug('Отладочная информация')
    # LOGGER_S.info('Информационное сообщение')
