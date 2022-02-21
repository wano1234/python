# Задача-1: Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

my_int = 5
my_float = 1.2
my_str = "Hello world"
my_list = ['a', '2']
my_tuple = ('b', '3')
my_dict = {'city': 'Moscow', 'country': 'Russia'}

# Задание-2: Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

super_list = [my_int, my_float, my_str, my_list, my_tuple, my_dict]
for i in super_list:
    print(f'{i} is {type(i)}')
    my_list = ['a', 'b', 'c', 'd', 'e']
    if len(my_list) % 2 == 0:
        i = 0
        while i < len(my_list):
            el = my_list[i]
            my_list[i] = my_list[i + 1]
            my_list[i + 1] = el
            i += 2
    else:
        i = 0
        while i < len(my_list) - 1:
            el = my_list[i]
            my_list[i] = my_list[i + 1]
            my_list[i + 1] = el
            i += 2
    print(my_list)
