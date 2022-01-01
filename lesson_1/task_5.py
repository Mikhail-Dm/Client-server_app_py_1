"""
    5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из байтового в строковый
        (предварительно определив кодировку выводимых сообщений).
"""

import subprocess

args1 = ['ping', 'yandex.ru']
args2 = ['ping', 'youtube.com']
num = 0

subproc_ping = subprocess.Popen(args1, stdout=subprocess.PIPE)
for line in subproc_ping.stdout:
    line = line.decode('cp866').encode('utf-8')
    args1 = line.decode('utf-8')
    num += 1
    if num > 0:
        break

subproc_ping = subprocess.Popen(args2, stdout=subprocess.PIPE)
for line in subproc_ping.stdout:
    line = line.decode('cp866').encode('utf-8')
    args2 = line.decode('utf-8')
    num += 1
    if num > 1:
        break

print()
print(args1)
print(args2)