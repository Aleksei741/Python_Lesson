# Написать два алгоритма нахождения i-го по счёту простого числа.
# Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
# Проанализировать скорость и сложность алгоритмов.
# Первый — с помощью алгоритма «Решето Эратосфена».
# Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков.
# Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.
# Второй — без использования «Решета Эратосфена».
# Примечание. Вспомните классический способ проверки числа на простоту.

import cProfile


def eratosfen(n):
    sieve = [i for i in range(n)]
    sieve[1] = 0

    for i in range(2, n):
        if sieve[i] != 0:
            j = i * 2

            while j < n:
                sieve[j] = 0
                j += i
    result = [i for i in sieve if i != 0]
    return (result)


def find_with_eratosfen(n):
    if n == 0:
        return 1
    result_eratosfen = {1}
    k = n
    while len(result_eratosfen) < n + 1:
        k += 1
        result_eratosfen = eratosfen(k)
    return result_eratosfen[n - 1]


def find_prime_number(n):
    operation = 1
    nuber = 0
    while nuber != n:
        operation += 1
        k = operation
        while k != 1:
            k -= 1
            if operation % k == 0 and k != 1:
                break
        else:
            nuber += 1
    return operation


# не надо i=0 это приведет к неверному результату
i = 1
# print('i = ', i)
# print(find_with_eratosfen(i))
# print(find_prime_number(i))

# python -m timeit -n 100 -s "import task2" "task2.find_with_eratosfen(10)"
# 100 loops, best of 5: 130 usec per loop
# python -m timeit -n 100 -s "import task2" "task2.find_with_eratosfen(50)"
# 100 loops, best of 5: 6.54 msec per loop
# python -m timeit -n 100 -s "import task2" "task2.find_with_eratosfen(100)"
# 100 loops, best of 5: 40.1 msec per loop
# python -m timeit -n 100 -s "import task2" "task2.find_with_eratosfen(200)"
# 100 loops, best of 5: 226 msec per loop

# python -m timeit -n 100 -s "import task2" "task2.find_prime_number(10)"
# 100 loops, best of 5: 30.3 usec per loop
# python -m timeit -n 100 -s "import task2" "task2.find_prime_number(50)"
# 100 loops, best of 5: 1.61 msec per loop
# python -m timeit -n 100 -s "import task2" "task2.find_prime_number(100)"
# 100 loops, best of 5: 9.32 msec per loop
# python -m timeit -n 100 -s "import task2" "task2.find_prime_number(200)"
# 100 loops, best of 5: 51 msec per loop

i = 1000
cProfile.run('find_with_eratosfen(i)')
# i = 10
#       ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        22    0.000    0.000    0.000    0.000 task2.py:12(eratosfen)
#        22    0.000    0.000    0.000    0.000 task2.py:13(<listcomp>)
#        22    0.000    0.000    0.000    0.000 task2.py:23(<listcomp>)
#         1    0.000    0.000    0.000    0.000 task2.py:27(find_with_eratosfen)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        23    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# i = 100
#       ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.041    0.041 <string>:1(<module>)
#       448    0.032    0.000    0.040    0.000 task2.py:12(eratosfen)
#       448    0.004    0.000    0.004    0.000 task2.py:13(<listcomp>)
#       448    0.005    0.000    0.005    0.000 task2.py:23(<listcomp>)
#         1    0.000    0.000    0.041    0.041 task2.py:27(find_with_eratosfen)
#         1    0.000    0.000    0.041    0.041 {built-in method builtins.exec}
#       449    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# i = 1000
#      ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000   10.377   10.377 <string>:1(<module>)
#      6928    8.573    0.001   10.305    0.001 task2.py:12(eratosfen)
#      6928    0.788    0.000    0.788    0.000 task2.py:13(<listcomp>)
#      6928    0.944    0.000    0.944    0.000 task2.py:23(<listcomp>)
#         1    0.071    0.071   10.377   10.377 task2.py:27(find_with_eratosfen)
#         1    0.000    0.000   10.377   10.377 {built-in method builtins.exec}
#      6929    0.001    0.000    0.001    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run('find_prime_number(i)')
# i = 10
#       ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 task2.py:38(find_prime_number)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# i = 100
#       ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.009    0.009 <string>:1(<module>)
#         1    0.009    0.009    0.009    0.009 task2.py:38(find_prime_number)
#         1    0.000    0.000    0.009    0.009 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# i = 1000
#       ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    2.322    2.322 <string>:1(<module>)
#         1    2.322    2.322    2.322    2.322 task2.py:38(find_prime_number)
#         1    0.000    0.000    2.322    2.322 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# Обыскал весь интернет, но не нашел способа адаптировать решето эратосфена под текущую задачу.
# Сам сделал это както криво, что отобразилось на производительности
