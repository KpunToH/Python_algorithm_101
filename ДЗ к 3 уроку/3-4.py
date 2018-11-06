# Определить, какое число в массиве встречается чаще всего


# Здесь будет заданный массив для удобства проверки кода.
first_list = [0, 1, 43, 0, 4, 1, 5, 0 , 5, 5, 5, 6, 5, 43, -5, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 5, 5, 5, 5, -6, 5]
print(first_list)
counter_max = 0
max_times_seen = ()

for i in first_list:
    counter = 0
    for j in first_list:
        if i == j:
            counter += 1
            if counter >= counter_max:
                counter_max = counter
                max_times_seen = i

print(f"Число {max_times_seen} встречалось чаще всего: {counter_max} раз")



