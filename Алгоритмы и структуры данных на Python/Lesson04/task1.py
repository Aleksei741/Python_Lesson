# 4. Найти сумму n элементов следующего ряда чисел:
# 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с клавиатуры.

# 1. Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых трех уроков.
# Примечание. Идеальным решением будет:
# a. выбрать хорошую задачу, которую имеет смысл оценивать,
# b. написать 3 варианта кода (один у вас уже есть),
# c. проанализировать 3 варианта и выбрать оптимальный,
# d. результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),
# e. написать общий вывод: какой из трёх вариантов лучше и почему.

import cProfile

def sum_elem1(n):
    element = 1
    sum = 0
    for i in range(n):
        sum += element
        element /= -2
    return (sum)


def sum_elem2(n):
    if n == 0:
        return 0
    elements = [1]
    for i in range(1, n):
        elements.append(elements[i - 1] / -2)
    return (sum(elements))


def sum_elem3(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    element = 1
    for i in range(n-1):
        element /= -2
    result = sum_elem3(n - 1) + element
    return (result)


k = 9000


#cProfile.run('sum_elem1(k)')
    # k = 900
    #   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    #         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
    #         1    0.000    0.000    0.000    0.000 task1.py:6(sum_elem1)
    #         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
    #         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

    # k = 9000
    #   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    #         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
    #         1    0.001    0.001    0.001    0.001 task1.py:6(sum_elem1)
    #         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
    #         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#cProfile.run('sum_elem2(k)')
    # k = 900
    #percall  cumtime  percall filename:lineno(function)
    #   1    0.000    0.000    0.000    0.000 <string>:1(<module>)
    #   1    0.000    0.000    0.000    0.000 task1.py:15(sum_elem2)
    #   1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
    #   1    0.000    0.000    0.000    0.000 {built-in method builtins.sum}
    # 899    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
    #   1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

    # k = 9000
    # percall  cumtime  percall filename:lineno(function)
    #   1    0.000    0.000    0.003    0.003 <string>:1(<module>)
    #   1    0.002    0.002    0.003    0.003 task1.py:15(sum_elem2)
    #   1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
    #   1    0.000    0.000    0.000    0.000 {built-in method builtins.sum}
    #8999    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
    #   1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#cProfile.run('sum_elem3(k)')
    #k=900
    #   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    #     1    0.000    0.000    0.022    0.022 <string>:1(<module>)
    # 900/1    0.022    0.000    0.022    0.022 task1.py:24(sum_elem3)
    #     1    0.000    0.000    0.023    0.023 {built-in method builtins.exec}
    #     1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

    # k = 9000
    # Переполнение стека

#==================================================================================================

#timeit:

#python -m timeit -n 1000 -s "import task1" "task1.sum_elem1(100)"
#1000 loops, best of 5: 6.86 usec per loop
#python -m timeit -n 1000 -s "import task1" "task1.sum_elem1(1000)"
#1000 loops, best of 5: 75 usec per loop
#python -m timeit -n 1000 -s "import task1" "task1.sum_elem1(10000)"
#1000 loops, best of 5: 804 usec per loop

#python -m timeit -n 1000 -s "import task1" "task1.sum_elem2(100)"
#1000 loops, best of 5: 15.4 usec per loop
#python -m timeit -n 1000 -s "import task1" "task1.sum_elem2(1000)"
#1000 loops, best of 5: 174 usec per loop
#python -m timeit -n 1000 -s "import task1" "task1.sum_elem2(10000)"
#1000 loops, best of 5: 1.81 msec per loop

#python -m timeit -n 1000 -s "import task1" "task1.sum_elem3(100)"
#1000 loops, best of 5: 262 usec per loop
#python -m timeit -n 1000 -s "import task1" "task1.sum_elem3(900)"
#1000 loops, best of 5: 20.7 msec per loop

#Вывод
#Самый лучший первый вариант. тк. Расчет суммы элементов и расчет элементов происходят паралельно.
#Второй вариант сначала рисчитывает элементы, затем производит сложение всех элементов выборки. Алгоритм заметно длинее первого
#Третий вариант абсолютно не жизнеспособен. начиная с того, что число больше (примерно) 900 вызывает ошибку по привышению стека
# Заканчивая временем выполнения. Вобщем добавлен сюда для выполнения требований задания.



