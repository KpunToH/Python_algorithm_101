# Написать два алгоритма нахождения i-го по счёту простого числа.
# Без использования Решета Эратосфена;
# Использовать алгоритм решето Эратосфена

import timeit
import cProfile

def eratosfen():
    # Взято из методички
    n = int(input("вывод простых чисел до числа ... "))
    a = [0] * n  # создание массива с n количеством элементов
    for i in range(n):  # заполнение массива ...
        a[i] = i  # значениями от 0 до n-1

    # вторым элементом является единица, которую не считают простым числом
    # забиваем ее нулем.
    a[1] = 0

    m = 2  # замена на 0 начинается с 3-го элемента (первые два уже нули)
    while m < n:  # перебор всех элементов до заданного числа
        if a[m] != 0:  # если он не равен нулю, то
            j = m * 2  # увеличить в два раза (текущий элемент - простое число)
            while j < n:
                a[j] = 0  # заменить на 0
                j = j + m  # перейти в позицию на m больше
        m += 1

    # вывод простых чисел на экран (может быть реализован как угодно)
    b = []
    for i in a:
        if a[i] != 0:
            b.append(a[i])

    del a
    print(b)

# Результаты профайлинга при выводе до 100000:
#          9601 function calls in 10.863 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.087    0.087   10.862   10.862 4-2.py:8(eratosfen)
#         1    0.001    0.001   10.863   10.863 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 codecs.py:319(decode)
#         1    0.000    0.000    0.000    0.000 codecs.py:331(getstate)
#         1    0.000    0.000    0.000    0.000 {built-in method _codecs.utf_8_decode}
#         1    0.000    0.000   10.863   10.863 {built-in method builtins.exec}
#         1   10.767   10.767   10.768   10.768 {built-in method builtins.input}
#         1    0.007    0.007    0.007    0.007 {built-in method builtins.print}
#      9592    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# Результаты timeit для вывода до 100000:
# Первый прогон - 0.01611867299999936
# Второй прогон - 0.013692006000000312
# Третий прогон - 0.013466672999999929

def not_eratosfen():
    n = int(input("вывод простых чисел до числа ... "))
    simple_numbers = []
    for i in range(2, n + 1):
        for j in simple_numbers:
            if i % j == 0:
                break
        else:
            simple_numbers.append(i)
    print(simple_numbers)

print(timeit.timeit(f"{not_eratosfen()}"))

# Результаты профайлинга для вывода до 100000
#
#          9601 function calls in 14.759 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    9.605    9.605   14.758   14.758 4-2.py:59(not_eratosfen)
#         1    0.000    0.000   14.759   14.759 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 codecs.py:319(decode)
#         1    0.000    0.000    0.000    0.000 codecs.py:331(getstate)
#         1    0.000    0.000    0.000    0.000 {built-in method _codecs.utf_8_decode}
#         1    0.000    0.000   14.759   14.759 {built-in method builtins.exec}
#         1    5.148    5.148    5.148    5.148 {built-in method builtins.input}
#         1    0.003    0.003    0.003    0.003 {built-in method builtins.print}
#      9592    0.003    0.000    0.003    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# Результаты timeit:
# Первый прогон - 0.015792450999999375
# Второй прогон - 0.01443067300000056
# Третий прогон - 0.015601785000000312
#  Сложность - хм.. O(n**2)?

