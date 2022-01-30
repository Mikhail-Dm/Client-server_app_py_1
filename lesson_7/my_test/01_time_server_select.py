import time
import select
from socket import socket, AF_INET, SOCK_STREAM


def new_listen_socket(address):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(address)
    sock.listen(1)
    sock.settimeout(0.9)  # Таймаут для операций с сокетом
    # Таймаут необходим, чтобы не ждать появления данных в сокете
    return sock


def mainloop():
    '''
    Основной цикл обработки запросов клиентов
    '''
    address = ('', 8888)
    clients = []
    sock = new_listen_socket(address)

    while True:
        try:
            conn, addr = sock.accept()  # Проверка подключений
        except OSError as e:
            pass  # timeout вышел
        else:
            print("Получен запрос на соединение с %s" % str(addr))
            clients.append(conn)
        finally:
            # Проверить наличие событий ввода-вывода без таймаута
            w = []
            try:
                r, w, e = select.select([], clients, [], 0)
            except Exception as e:
                # Исключение произойдет, если какой-то клиент отключится
                pass  # Ничего не делать, если какой-то клиент отключился

            # Обойти список клиентов, читающих из сокета
            for s_client in w:
                timestr = time.ctime(time.time()) + "\n"
                try:
                    s_client.send(timestr.encode('utf-8'))
                except:
                    # Удаляем клиента, который отключился
                    clients.remove(s_client)


print('Эхо-сервер запущен!')
mainloop()
