"""
    3. Задание на закрепление знаний по модулю yaml.
    Написать скрипт, автоматизирующий сохранение данных в файле YAML-формата. Для этого:

        Подготовить данные для записи в виде словаря, в котором
                первому ключу соответствует список,
                второму — целое число,
                третьему — вложенный словарь, где значение каждого ключа — это целое число с юникод-символом,
                    отсутствующим в кодировке ASCII (например, €);

        Реализовать сохранение данных в файл формата YAML — например, в файл file.yaml.
            При этом обеспечить стилизацию файла с помощью параметра default_flow_style, а также установить
            возможность работы с юникодом: allow_unicode = True;

        Реализовать считывание данных из созданного файла и проверить, совпадают ли они с исходными.
"""

import yaml
import io
import pprint


data = {
    'a list': ['str1', 'str2', 'str3', 'str4'],
    'b num': 10,
    'c dict': {
        'param1': 'str€',
        'param2': 'str€',
        'param3': 13
    }
}


with io.open('to_solve/data.yaml', 'w', encoding='utf8') as outfile:
    yaml.dump(data, outfile, default_flow_style=False, allow_unicode=True)

with open('to_solve/data.yaml', 'r') as stream:
    data_loaded = yaml.safe_load(stream)
pprint.pprint(data_loaded)
