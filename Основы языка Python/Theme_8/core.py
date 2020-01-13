import os
import shutil
import datetime


def create_file(name, text=None):
    with open(name, 'w', encoding='utf-8') as f:
        if text:
            f.write(text)


def create_folder(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print('Такая папка уже есть')


def get_list(folders_only=False):
    result = os.listdir()
    if folders_only:
        result = [f for f in result if os.path.isdir(f)]
    print(result)


def change_directory(name = None):
    if name == None:
        list_name = os.path.split(os.path.abspath(os.curdir))
        os.chdir(list_name[0])
    elif os.path.isdir(name):
        os.chdir(name)
    else:
        print('Данный путь не является папкой')
    print('Текущая рабочая деректория: ' + os.path.abspath(os.curdir))


def delete_file(name):
    if os.path.isdir(name):
        os.rmdir(name)
    else:
        os.remove(name)


def copy_file(name, new_name):
    if os.path.isdir(name):
        try:
            shutil.copytree(name, new_name)
        except FileExistsError:
            print('Такая папка уже есть')
    else:
        shutil.copy(name, new_name)


def save_info(massage, curdir = None):
    current_time = datetime.datetime.now()
    result = f'{current_time} - {massage}'
    if curdir == None:
        with open('log.txt', 'a', encoding='utf-8') as f:
            f.write(result + '\n')
    else:
        with open(os.path.join(curdir, 'log.txt'), 'a', encoding='utf-8') as f:
            f.write(result + '\n')
    return os.path.abspath(os.curdir)


if __name__ == '__main__':
    dat1 = save_info('1')
    print(dat1)
    dat2 = save_info('q', dat1)
    print(dat2)
