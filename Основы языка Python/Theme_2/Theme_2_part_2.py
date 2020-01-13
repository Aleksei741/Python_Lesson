days = (
    	'первое',
	'второе',
	'третье',
	'четвертое',
	'пятое',
	'шестое',
	'седьмое',
	'восьмое',
	'девятое',
	'десятое',
	'одиннадцатое',
	'двенадцатое',
	'тринадцатое',
	'четырнадцатое',
	'пятнадцатое',
	'шестнадцатое',
	'семьнадцатое',
	'восемьнадцатое',
	'девятнадцатое',
	'двадцатое',
	'двадцать первое',
	'вадцать второе',
	'двадцать третье',
	'двадцать четвертое',
	'двадцать пятое',
	'двадцать шестое',
	'двадцать седьмое',
	'двадцать восьмое',
	'двадцать девятое',
	'тридцатое',
	'тридцать первое'
        )

months = (
        'января',
	'февраля',
	'марта',
	'апреля',
	'мая',
	'июня',
	'июля',
	'августа',
	'сентября',
	'октября',
	'ноября',
	'декабря'
        )

years = (
    'двухтысячного',
    'две тысячи первого',
    'две тысячи второго',
    'две тысячи третьего',
    'две тысячи четвертого',
    'две тысячи пятого',
    'две тысячи шестого',
    'две тысячи седьмого',
    'две тысячи восьмого',
    'две тысячи девятого',
    'две тысячи десятого',
    'две тысячи одиннадцатого',
    'две тысячи двенадцатого',
    'две тысячи тринадцатого',
    'две тысячи четырнадцатого',
    'две тысячи пятнадцатого',
    'две тысячи шестнадцатого',
    'две тысячи семнадцатого',
    'две тысячи вомнадцатого',
    'две тысячи девятнадцатого'
    )

#data_str = '19.12.2000'
data_str = input('Введите дату в формате dd.mm.yyyy: ')

data_list = data_str.split('.')

if(len(data_list) == 3):    
    if (0 < int(data_list[0]) <= 31) and (0 < int(data_list[1]) <= 12) and data_list[2].isdigit():
        if (2000 <= int(data_list[2]) <= 2019):
            print('{} {} {} года'.format(days[int(data_list[0]) - 1], months[int(data_list[1]) - 1], years[int(data_list[2]) - 2000]))
        else:
            print('{} {} {} года'.format(days[int(data_list[0]) - 1], months[int(data_list[1]) - 1], data_list[2]))
    else:
        print('некорректные данные')
else:
    print('некорректные данные')

