"""
    6. Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет», «декоратор».
    Проверить кодировку созданного файла (исходить из того, что вам априори неизвестна кодировка этого файла!).
    Затем открыть этот файл и вывести его содержимое на печать.

    ВАЖНО: файл должен быть открыт без ошибок вне зависимости от того, в какой кодировке он был создан!
"""

from chardet.universaldetector import UniversalDetector


some_list = ['сетевое программирование', 'сокет', 'декоратор']
with open('test_file.txt', 'w') as f:
    for i in some_list:
        f.write(f'{i}\n')

detector = UniversalDetector()
with open('test_file.txt', 'rb') as fh:
    for line in fh:
        detector.feed(line)
        if detector.done:
            break
    detector.close()
enc_file = detector.result.get('encoding')

some_list = []
with open('test_file.txt', 'r', encoding=enc_file) as f:
    print()
    for line in f:
        some_list.append(line.rstrip())

print(some_list)