# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.


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
print(f"Позиция минимума {i_min_index}, позиция максимума {i_max_index}")


second_list = first_list[:]
second_list.remove(i_max)
second_list.remove(i_min)
second_list.insert(i_min_index, i_max)
second_list.insert(i_max_index, i_min)
print(second_list)