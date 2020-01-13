#import sys

def num_math(num = 13):
    if num == 13:
        raise Exception ('13 нехорошее число')
    elif not (0 < num <= 100):
        raise Exception('Число {} лежит вне диапазона обработки функции'.format(num))
    return num**2
try:
    number = int(input('Введите число: '))
except Exception as e:
    print('Полюбуйтесь, что вы натворили: {}'.format(e))
    #sys.exit();
else:
    try:
        result = num_math(number)
    except Exception as e:
        print('Возникла исключительная ситуёвина: {}'.format(e))
    else:
        print(result)
