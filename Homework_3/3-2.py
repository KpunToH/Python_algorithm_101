# 2.	Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив надо
# заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля),
#  т.к. именно в этих позициях первого массива стоят четные числа.


import random


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
