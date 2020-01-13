# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется
# как массив,
# элементы которого — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
# произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
# Примечание: Если воспользоваться функциями hex() и/или int() для преобразования систем счисления,
# задача решается в несколько строк.
# Для прокачки алгоритмического мышления такой вариант не подходит.
# Поэтому использование встроенных функций для перевода из
# одной системы счисления в другую в данной задаче под запретом.

from collections import ChainMap

list_of_numbers = [str(i) for i in range(10)] + ['A', 'B', 'C', 'D', 'E', 'F']
dict_num_to_HEX = {}
dict_HEX_to_num = {}
for i in list_of_numbers:
    dict_num_to_HEX[list_of_numbers.index(i)] = i
for i in list_of_numbers:
    dict_HEX_to_num[i] = list_of_numbers.index(i)
dict_none = {}
dict_none[None] = 0

numbers = ChainMap(dict_num_to_HEX, dict_HEX_to_num, dict_none)


def sum_HEX(A='0', B='0'):
    list_A = A[::-1]
    list_B = B[::-1]
    flag = 0
    result = list()
    for i in range(max(len(list_A), len(list_B))):
        index_A = list_A[i] if i < len(list_A) else '0'
        index_B = list_B[i] if i < len(list_B) else '0'
        r = numbers[index_A] + numbers[index_B] + flag
        if r > 15:
            r -= 16
            flag = 1
        else:
            flag = 0
        result.append(numbers[r])

    if flag == 1:
        result.append('1')
    return ''.join(result[::-1])

def Multiplication_HEX(A='0', B='0'):
    list_A = list(A[::-1])
    list_B = list(B[::-1])
    result = list()

    for i in range(len(list_B)):
        j = 0
        flag_j = 0
        result.append(list())
        while flag_j != 0 or len(result[i]) == 0 or j <= len(list_A):
            index_A = list_A[j] if j < len(list_A) else '0'
            index_B = list_B[i] if i < len(list_B) else '0'
            r = numbers[index_A] * numbers[index_B] + flag_j
            flag_j //= 16
            while r > 15:
                r -= 16
                flag_j += 1
            j += 1
            result[i].append(numbers[r])
        bufer = i
        while bufer > 0:
            bufer -= 1
            result[i].insert(0, '0')

    sum_HEX_ = '0'
    for i in range(len(result)):
        sum_HEX_ = sum_HEX(sum_HEX_, ''.join(result[i][::-1]))

    return sum_HEX_


first = input('Первое число: ')
second = input('Второе число: ')

print(f'Сумма: {sum_HEX(first, second)}')
print(f'Не сумма: {Multiplication_HEX(first, second)}')
