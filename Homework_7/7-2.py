# Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
#  заданный случайными числами на промежутке [0; 50).
#  Выведите на экран исходный и отсортированный массивы.

import random


LEN_RAN = 10
array = [random.random()*50 for el in range(LEN_RAN)]
print(f"исходный массив {array}")


def mergeSort(x):
    if len(x) > 1:
        center = len(x) // 2
        left_side = x[:center]
        right_side = x[center:]

        mergeSort(left_side)
        mergeSort(right_side)

        i = 0
        j = 0
        k = 0
        while i < len(left_side) and j < len(right_side):
            if left_side[i] < right_side[j]:
                x[k] = left_side[i]
                i = i + 1
            else:
                x[k] = right_side[j]
                j = j + 1
            k = k + 1

        while i < len(left_side):
            x[k] = left_side[i]
            i = i + 1
            k = k + 1

        while j < len(right_side):
            x[k] = right_side[j]
            j = j + 1
            k = k + 1

mergeSort(array)
print(f"Отсортированный слиянием список {array}")