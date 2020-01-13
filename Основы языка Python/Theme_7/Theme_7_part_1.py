import random

Available_Fruits = (
    'Абрикос',
    'Авокадо',
    'Австромиртус сладкий',
    'Азимина',
    'Айва',
    'Акебия',
    'Ананас',
    'Антильский абрикос',
    'Апельсин',
    'Араза',
    'Архат',
    'Баккорея Мотли',
    'Бакупари',
    'Барбадосская вишня',
    'Белая сапота',
    'Билимби',
    'Бирсонима толстолистная',
    'Боярышник мексиканский',
    'Бромелия пингвин',
    'Бунхозия серебристая',
    'Вампи',
    'Вишня (плод)',
    'Воаванга',
    'Восковница красная',
    'Гандария',
    'Гарциния индийская',
    'Гарциния Ливингстона',
    'Гарциния Прейна',
    'Генипа американская',
    'Груша',
    'Лайм',
    'Лимон',
    'Малина майсорская',
    'Малина пурпурноплодная',
    'Манго (фрукт)',
    'Мандарин',
    'Маракуйя (фрукт)',
    'Нектарин',
    'Папайя',
    'Помело (фрукт)',
    'Фикус',
    'Хлебное дерево',
    'Хурма'
    )

len_1 = random.randint(10, len(Available_Fruits) - 20)
len_2 = random.randint(10, len(Available_Fruits) - 20)

Fruits_list_1 = random.sample(Available_Fruits, len_1)
Fruits_list_2 = random.sample(Available_Fruits, len_2)

print('Первый список фруктов длиной {}:'.format(len_1))
for fruit in Fruits_list_1:
    print('{:>25}'.format(fruit), end='; ')

print('\nВторой список фруктов длиной {}:'.format(len_2))
for fruit in Fruits_list_2:
    print('{:>25}'.format(fruit), end='; ')
print('')
Final_list = list(set(Fruits_list_1) & set(Fruits_list_2))

print('Список фруктов, присутствующих в обоих исходных списках длиной {}:'.format(len(Final_list)))
for fruit in Final_list:
    print('{:>25}'.format(fruit), end='; ')