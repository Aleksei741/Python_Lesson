import sys
from game_guess_number import game
from core import create_file, create_folder, get_list, delete_file, copy_file, save_info, change_directory

adderss = save_info('Старт')
command = ''

try:
    command = sys.argv[1]
except IndexError:
    print('Пустая команда')
else:
    save_info(sys.argv[1:])

if command == 'list':
    get_list()
elif command == 'create_file':
    try:
        name = sys.argv[2]
    except IndexError:
        print('Отсутствует название файла')
    else:
        create_file(name)
elif command == 'create_folder':
    try:
        name = sys.argv[2]
    except IndexError:
        print('Отсутствует название папки')
    else:
        create_folder(name)
elif command == 'delete':
    try:
        name = sys.argv[2]
    except IndexError:
        print('Отсутствует название')
    else:
        delete_file(name)
elif command == 'copy':
    try:
        name = sys.argv[2]
        new_name = sys.argv[3]
    except IndexError:
        print('Отсутствует название папки или файла')
    else:
        copy_file(name, new_name)
elif command == 'cd':
    try:
        name = sys.argv[2]
    except IndexError:
        change_directory()
    else:
        change_directory(name)
elif command == 'game':
    game()
elif command == 'help':
    print('list - список файлов и папок')
    print('create_file - создание файла')
    print('create_folder - создание папки')
    print('delete - удаление файла или папки')
    print('copy - копирование файла или папки')
    print('cd - Смена текущей деректории')
    print('game - Для отдыха')


save_info('Конец', adderss)
