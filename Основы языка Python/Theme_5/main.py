import Theme_5_part_1
from Theme_5_part_2 import rand_list

Theme_5_part_1.creat_folder()
input('Директории от dir_1 до dir_9 созданы. Нажмите Enter чтобы удалить')
Theme_5_part_1.remove_folder()
input('Директории от dir_1 до dir_9 удалены. Нажмите Enter чтобы продолжить')

my_list = [1, 2, 3, 4]
print('Список: {}'.format(my_list))
print('Случайный элемент из списка: {}'.format(rand_list(my_list)))
my_list = []
print('Список: {}'.format(my_list))
print('Случайный элемент из списка: {}'.format(rand_list(my_list)))
input('Нажмите Enter')


