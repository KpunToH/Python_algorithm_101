# 2.	Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив надо
# заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля),
#  т.к. именно в этих позициях первого массива стоят четные числа.


import random
import sys

RAZMER = random.randint(0, 20)
first_list = [random.randint(0, RAZMER * RAZMER) for _ in range(RAZMER)]
print(first_list)

# Если не пронумеровать элементы - возникают проблемы с ссылками на дублирующиеся значения
first_list_enumerated = list(enumerate(first_list))
second_list = []

for i, j in first_list_enumerated:
    if j % 2 == 0:
        second_list.append(i)

# Индексация - с нуля!
print(second_list)

def variables_memory():
    """
    :Анализ затрат памяти всех неслужебных переменных:
    """
    variables = globals().copy()
    for i in variables.copy():
        if i.startswith("__") == 1 or i in ["variables_memory", "sys", "random"]:
            del variables[i]
    print(f"Список переменных программы {variables}")

    memory_usage = []
    for j in variables.values():
        memory_usage.append(sys.getsizeof(j))
    print(f"Использование памяти переменными {memory_usage}")
    print(f"Суммарное использование памяти переменными основной программы {(sum(memory_usage))}")

variables_memory()

# python 3.7, x64
# Результаты теста - Список переменных программы {'RAZMER': 12,
#   'first_list': [70, 32, 22, 112, 90, 25, 134, 66, 18, 108, 120, 24],
#   'first_list_enumerated': [(0, 70), (1, 32), (2, 22), (3, 112), (4, 90),
#   (5, 25), (6, 134), (7, 66), (8, 18), (9, 108), (10, 120), (11, 24)],
#    'second_list': [0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11],
#    'i': 11, 'j': 24}
# Использование памяти переменными [14, 100, 84, 100, 14, 14]
# Суммарное использование памяти переменными основной программы 326
