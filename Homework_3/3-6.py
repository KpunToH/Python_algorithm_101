# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать

import random

RAZMER = random.randint(0, 20)
first_list = [random.randint(0, RAZMER*RAZMER) for _ in range(RAZMER+1)]
print(first_list)

i_max = 0
i_min = RAZMER * RAZMER

for i in first_list:
    if i >= i_max:
        i_max = i
        i_max_index = first_list.index(i)
    if i <= i_min:
        i_min = i
        i_min_index = first_list.index(i)

print(f"Максимум равен {i_max}, минимум равен {i_min}")

if i_min_index>i_max_index:
    i_min_index, i_max_index = i_max_index, i_min_index

min_max_list = first_list[i_min_index+1: i_max_index]
print(f"Элементы между минимальным и максимальным значением {min_max_list}")

summa = sum(el for el in min_max_list)
print(f"Сумма элементов между минимумом и максимумом равна {summa}")
