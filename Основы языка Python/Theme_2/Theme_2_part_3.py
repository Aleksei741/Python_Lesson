

len_input_list = int(input('Введите длину списка: '))
input_list = []

for i in range(len_input_list):
    input_list.append(input('Введите {} элемент списка: '.format(i)))

#input_list = [2, 2, 5, 12, 8, 2, 12]

output_list = []
for i in input_list:
    if input_list.count(i) == 1:
        output_list.append(i)

print(output_list)
