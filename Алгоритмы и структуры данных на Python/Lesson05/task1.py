# 1. Пользователь вводит данные о количестве предприятий, их наименования
# и прибыль за 4 квартал для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий)
# и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

from collections import defaultdict, namedtuple

data_format_profir = ('profit1', 'profit2', 'prifit3', 'profit4')
profit = namedtuple('profit', data_format_profir)

input_data = defaultdict(profit)

#Закоментируй тут
n = int(input('Введите количество предприятий: '))
for i in range(n):
    name = input(f'Введите название {i + 1} предприятия: ')
    prof = list(range(4))
    for j in range(4):
        prof[j] = int(input(f'Введите прибыль за {j + 1} квартал: '))
    input_data[name] = (prof[0], prof[1], prof[2], prof[3])
##############################################

#раскоментируй тут
# input_data['company1'] = (300, 400, 350, 500)
# input_data['company2'] = (600, 400, 750, 800)
# input_data['company3'] = (100, 800, 350, 200)
# input_data['company4'] = (500, 100, 750, 200)
##############################################

output_data = defaultdict(int)

for i in input_data:
    sum = 0
    for j in input_data[i]:
        sum += j
    output_data[i] = sum / 4

print('Средняя прибыль: ')
for i in output_data:
    print(f'{i}   {output_data[i]}')

average_value = 0
for i in output_data:
    average_value += output_data[i]
average_value /= len(output_data)

print('Прибыль выше среднего: ')
for i in output_data:
    if output_data[i] > average_value:
        print(f'{i}   {output_data[i]}')

print('Прибыль ниже среднего: ')
for i in output_data:
    if output_data[i] <= average_value:
        print(f'{i}   {output_data[i]}')

# print(input_data)
