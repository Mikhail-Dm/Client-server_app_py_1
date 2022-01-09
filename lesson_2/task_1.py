"""
    1. Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий выборку определенных данных
    из файлов info_1.txt, info_2.csv, info_3.csv и формирующий новый «отчетный» файл в формате CSV. Для этого:

        Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными, их открытие и
        считывание данных.
            В этой функции из считанных данных необходимо с помощью регулярных выражений извлечь значения параметров:
                «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».

            Значения каждого параметра поместить в соответствующий список. Должно получиться четыре списка — например,
                os_prod_list, os_name_list, os_code_list, os_type_list.

            В этой же функции создать главный список для хранения данных отчета — например, main_data — и поместить
            в него названия столбцов отчета в виде списка:
                «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».

            Значения для этих столбцов также оформить в виде списка и поместить в файл main_data
            (также для каждого файла);


        Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл.
            В этой функции реализовать получение данных через вызов функции get_data(), а также сохранение
            подготовленных данных в соответствующий CSV-файл;

            Проверить работу программы через вызов функции write_to_csv().
"""

import csv


def get_data():
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    main_data = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']
    for i in range(1, 4):
        with open(f'to_solve/info_{i}.txt', encoding='utf-8') as f_n:
            for line in f_n:
                get_data_if_main_data('Изготовитель системы', os_prod_list, line)
                get_data_if_main_data('Название ОС', os_name_list, line)
                get_data_if_main_data('Код продукта', os_code_list, line)
                get_data_if_main_data('Тип системы', os_type_list, line)
    data = [main_data, os_prod_list, os_name_list, os_code_list, os_type_list]
    return data


def get_data_if_main_data(my_str, my_list, line):
    if my_str in line:
        line = line.replace(my_str, '').replace(':', '')
        line = ' '.join(line.split())
        my_list.append(line)


def write_to_csv(file_name):
    with open(f'{file_name}', 'w') as f_n:
        f_n_writer = csv.writer(f_n, quoting=csv.QUOTE_NONNUMERIC)
        data = get_data()
        f_n_writer.writerows(data)

    with open(f'{file_name}') as f_n:
        print(f_n.read())


write_to_csv('to_solve/write_to_csv.csv')
