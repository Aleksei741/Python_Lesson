
name = ''
surname = ''
age  = 0
weight = 0

#Ввод
name = input('Введите имя: ')
surname = input('Введите фамилию: ')
age = int(input('Введите колличество полных лет: '))
weight = int(input('Введите вес: '))

#Вывод шапки
print(name, surname, end = '')
print(',', age, end=' ')

if (age % 10) == 1:
    print('год', end=', ')
elif (age % 10) <= 4:
    print('годa', end=', ')
else:
    print('лет', end=', ')

print('вес', weight, end = ' - ')

#Вывод заключения
if(age < 30 and (weight >= 50 and weight < 120)):
    print('в хорошем состоянии')
elif(age >= 40 and (weight < 50 or weight >= 120)):
    print('требуется врачебный осмотр')
elif(age >= 30 and (weight < 50 or weight >= 120)):
    print('требуется заняться собой')
else:
    print('слишком хорош')
