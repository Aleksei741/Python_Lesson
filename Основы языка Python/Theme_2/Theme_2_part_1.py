import time
#my_list_1 = [2, 5, 8, 2, 12, 12, 4]
#my_list_2 = [2, 7, 12, 3]

print('Желаете использовать пример задания? y/n ', end = '')

answer = ' '
list_1 = []
list_2 = []

while (not answer == 'y') and (not answer == 'n'):
    answer = input( )
    
if answer == 'n':
    count_list_1 = int(input('Введите колличество элементов первого списка: '))

    for i in range(count_list_1):
        list_1.append(input('Введите {} элементов первого списка: '.format(i)))

    count_list_2 = int(input('Введите колличество элементов второго списка: '))

    for i in range(count_list_2):
        list_2.append(input('Введите {} элементов первого списка: '.format(i)))
elif answer == 'y':
    list_1 = [2, 5, 8, 2, 12, 12, 4]
    list_2 = [2, 7, 12, 3, 143]

print('первый список:')
print(list_1)
print('второй список:')
print(list_2)

for i in list_2:
    time.sleep(1)
    if i in list_1:
        print('элемент {:>3} yдаляем '.format(i))
        while(i in list_1):
            list_1.remove(i)
    else:
        print('элемент {:>3} нет в списке'.format(i))

print('От первого списка осталось только:')
print(list_1)
