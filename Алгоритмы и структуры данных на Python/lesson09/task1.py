# 1. Определение количества различных подстрок с использованием хеш-функции.
# Пусть на вход функции дана строка.
# Требуется вернуть количество различных подстрок в этой строке.
# Примечание: в сумму не включаем пустую строку и строку целиком.
# Пример работы функции:

# >>> func("papa")
# 6
# >>> func("sova")
# 9

import hashlib


def search_str(s: str, subs: str) -> int:
    assert len(s) > 0 and len(subs) > 0, 'Строки не могут быть пустыми'
    assert len(s) > len(subs), 'Подстрока должна быть меньше строки'

    len_sub = len(subs)
    h_subs = hashlib.sha1(subs.encode('utf-8')).hexdigest()

    count = 0

    for i in range(len(s) - len_sub + 1):
        if h_subs == hashlib.sha1(s[i:i + len_sub].encode('utf-8')).hexdigest():

            if s[i:i + len_sub] == subs:
                count += 1

    return count


s_1 = input('Введите строку: ')
s_2 = input('Введите подстроку: ')

cont = search_str(s_1, s_2)

print(f'Подстрока найдена {cont} раз')
