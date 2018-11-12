# Проанализировать скорость и сложность одного любого алгоритма,
#  разработанных в рамках домашнего задания первых трех уроков.
# В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны любому из чисел в диапазоне от 2 до 9.
#

import timeit
import cProfile

# Первый вариант
def homework_4():
    numbers = [_ for _ in range(2, 100)]
    deliteli = [_ for _ in range(2, 10)]
    counter = [0]*10
    for j in deliteli:
        for i in numbers:
             if i % j == 0:
                counter[j] += 1
        print(f"Число {j} является делителем {counter[j]} раз")

# Первый прогон - 20000000 loops, best of 5: 13.6 nsec per loop
# Второй прогон - 20000000 loops, best of 5: 13.4 nsec per loop
# Третий прогон - 20000000 loops, best of 5: 13.2 nsec per lsec per loop

# Результаты профайлинга функции для чисел от 0 до 100000 ( что б разница была видна)
#         14 function calls in 0.140 seconds
#   Ordered by: standard name
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.132    0.132    0.138    0.138 4-1.py:10(homework_4)
#        1    0.006    0.006    0.006    0.006 4-1.py:11(<listcomp>)
#        1    0.000    0.000    0.000    0.000 4-1.py:12(<listcomp>)
#        1    0.001    0.001    0.140    0.140 <string>:1(<module>)
#        1    0.000    0.000    0.140    0.140 {built-in method builtins.exec}
#        8    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

def homework_4_2():
    numbers = dict.fromkeys([_ for _ in range(2, 100)])
    deliteli = [_ for _ in range(2, 10)]
    for d in deliteli:
        cnt = 0
        for n in numbers:
            if n % d == 0:
                cnt += 1
        numbers[d] = cnt
        print(f"Число {d} является делителем {numbers[d]} раз")
#Результаты второго варианта:

# Первый прогон 20000000 loops, best of 5: 14.9 nsec per loop
# Второй прогон 20000000 loops, best of 5: 14.3 nsec per loop
# Третий прогон 20000000 loops, best of 5: 14.5 nsec per loop

# Результаты профайлинга для чисел от 0 до 100000 ( что б разница была видна)
# 15 function calls in 0.150 seconds
# Ordered by: standard name

#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.127    0.127    0.148    0.148 4-1.py:37(homework_4_2)
#        1    0.006    0.006    0.006    0.006 4-1.py:38(<listcomp>)
#        1    0.000    0.000    0.000    0.000 4-1.py:39(<listcomp>)
#        1    0.002    0.002    0.150    0.150 <string>:1(<module>)
#        1    0.000    0.000    0.150    0.150 {built-in method builtins.exec}
#        8    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#        1    0.015    0.015    0.015    0.015 {built-in method fromkeys}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# Вывод - "я все исправил к худшему!"
# Сложность алгоритма - вроде O(n), с увеличением кол-ва элементов время растет растет линейно.

print(cProfile.run("homework_4()"))
print(cProfile.run("homework_4_2()"))
