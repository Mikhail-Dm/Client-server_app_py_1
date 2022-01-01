"""
    2. Каждое из слов «class», «function», «method» записать в байтовом типе. Сделать это необходимо в автоматическом, а не
    ручном режиме с помощью добавления литеры b к текстовому значению, (т.е. ни в коем случае не используя методы encode и
    decode) и определить тип, содержимое и длину соответствующих переменных.
"""

some_list = ['class', 'function', 'method']
for i in some_list:
    print()
    some_word = eval(f"b'{i}'")
    print(f'type({type(some_word)})  =>  {some_word}   =>   {len(some_word)}')