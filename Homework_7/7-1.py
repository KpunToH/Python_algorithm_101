# Отсортировать по убыванию методом «пузырька» одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100).
# Вывести на экран исходный и отсортированный массивы.

import random


LEN_RAN = 10
buble_array = [random.randint(-100, 100) for el in range(LEN_RAN)]
print(f"исходный массив {buble_array}")

def bubleSort(x):
    '''
    Сортировка с сокращением лишних прогонов цикла в конце
    '''
    n = len(x)
    k = x[:]
    while n:
        for i in range(n - 1):
            if x[i] < x[i + 1]:
                x[i], x[i + 1] = x[i + 1], x[i]
                j = x[:]
                if k == j:
                    break
        n -= 1

bubleSort(buble_array)
print(f"отсортированный массив {buble_array}")

