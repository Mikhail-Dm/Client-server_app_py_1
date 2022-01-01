"""
    4. Преобразовать слова «разработка», «администрирование», «protocol», «standard»
    из строкового представления в байтовое и выполнить обратное преобразование (используя методы encode и decode).
"""

some_list = ['разработка', 'администрирование', 'protocol', 'standard']
for i in some_list:
    print()
    some_word_b = i.encode('utf-8')
    some_word = some_word_b.decode('utf-8')
    print(f'{some_word_b}  =>  {some_word}')