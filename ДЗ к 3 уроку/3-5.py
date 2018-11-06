# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

import random

# ТерВер говорит, что вероятность отсутсвия отрицательных чисел в таком массиве околонулевая,
# но вынуждает делать проверку на отрицательность;)
first_list = [random.randint(-100, 1) for _ in range(20)]
print(first_list)

counter_max = 0
max_minus = ()

for i in first_list:
    if i < 0:
        counter = 0
        for j in first_list:
            if i >= j:
                counter += 1
                if counter >= counter_max:
                    counter_max = counter
                    max_minus = i

print(f"Число {max_minus} на позиции {first_list.index(max_minus)} - наибольшее отрицательное число в массиве")
