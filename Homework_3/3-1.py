# В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны любому из чисел в диапазоне от 2 до 9.

numbers = [_ for _ in range(2, 100)]
deliteli = [_ for _ in range(2, 10)]
# 10 здесь используется потому, что я хочу список из 8 нулей + 2 места для избежания обращения к несуществующим ячейкам
counter = [0]*10
for j in deliteli:
    for i in numbers:
        if i % j == 0:
            counter[j] += 1
    print(f"Число {j} является делителем {counter[j]} раз")