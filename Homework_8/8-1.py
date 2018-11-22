# Определение количества различных подстрок с использованием хеш-функции.
# Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
# Требуется найти количество различных подстрок в этой строке.
import hashlib

def subs_counter (s):
    len_s = len(s)

    k = 0
    hash_lib = []
    while k < len_s:
        n = 1
        while n < len_s:
            divided_s = [s[i+k:i+n] for i in range(0, len(s), n)]
            for j in divided_s:
                if hashlib.sha1(j).hexdigest() not in hash_lib:
                    hash_lib.append(hashlib.sha1(j).hexdigest())
            n += 1
        k += 1

    print(f"Колличество подстрок равно {len(hash_lib)}")

subs_counter(input("введите строку из маленьких латинских букв ").encode('utf-8'))
