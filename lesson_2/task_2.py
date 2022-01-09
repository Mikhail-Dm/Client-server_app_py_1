"""
    2. Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с информацией о заказах.
    Написать скрипт, автоматизирующий его заполнение данными. Для этого:

        Создать функцию write_order_to_json(), в которую передается 5 параметров —
                товар (item), количество (quantity), цена (price), покупатель (buyer), дата (date).

            В это словаре параметров обязательно должны присутствовать юникод-символы, отсутствующие в кодировке ASCII.

            Функция должна предусматривать запись данных в виде словаря в файл orders.json.

            При записи данных указать величину отступа в 4 пробельных символа;

            Необходимо также установить возможность отображения символов юникода: ensure_ascii=False;

            Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого
            параметра.
"""

import json
import datetime
import pprint


# товар (item), количество (quantity), цена (price), покупатель (buyer), дата (date)
def write_order_to_json(item, quantity, price, buyer):
    now_date = datetime.date.today().strftime("%d/%m/%Y")
    params = [item, quantity, price, buyer, now_date]

    with open('to_solve/orders.json') as f:
        obj = json.load(f)
    obj['orders'].append(params)

    with open('to_solve/orders.json', 'w', encoding='utf-8') as f:
        json.dump(obj, f, ensure_ascii=False)


write_order_to_json('Костыль', 1, 599, 'Михаил')
write_order_to_json('Костыль', 1, 599, 'Константин')
with open('to_solve/orders.json') as f:
    pprint.pprint(f.read())


# можно выполнить очистку для других тестов с помощью кода ниже
# initial_data = {'orders': []}
# with open('to_solve/orders.json', 'w', encoding='utf-8') as f:
#     json.dump(initial_data, f)
