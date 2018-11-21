# Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой – не больше медианы.
# Задачу можно решить без сортировки исходного массива.

import random


m_input = int(input("Пожалуйста, введите натуральное число ""m"" для определения массива размером 2m + 1 "))
array_len = m_input * 2 + 1
array = [random.randint(-10, 10) for el in range(array_len)]
print(f"Исходный массив {array}")

def true_median_finder(x):
    '''
    Нахождение медианы массива с нечетным кол-вом элементов
    '''

    for i in x:
        left_side = x[:x.index(i)]
        right_side = x[(x.index(i)+1):]

        for m in left_side[:]:
            if m >= i:
                right_side.append(m)
                left_side.remove(m)

        for j in right_side[:]:
            if j <= i:
                left_side.append(j)
                right_side.remove(j)

        if len(left_side) == len(right_side):
            print(f"медиана массива равна {i}")
            break

true_median_finder(array)
