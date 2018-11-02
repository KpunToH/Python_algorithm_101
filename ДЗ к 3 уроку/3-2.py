# 2.	Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив надо
# заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля),
#  т.к. именно в этих позициях первого массива стоят четные числа.


import random


SIZE = 10
first_list = [random.randint(0, SIZE * SIZE) for _ in range(SIZE)]
print(first_list)
second_list = [0]*(SIZE+4)

for i in first_list:
    if first_list[i] % 2 == 0:
        second_list.append(i)

print(second_list)
