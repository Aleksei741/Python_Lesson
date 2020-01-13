import os

def creat_folder():
    for i in range(9):
        str = 'dir_{}'.format(i+1)
        print('Create:', end=' ')
        print(os.path.join(os.getcwd(), str))
        os.mkdir(str)

def remove_folder():
    for i in range(9):
        str = 'dir_{}'.format(i+1)
        print('Remove:', end = ' ')
        print(os.path.join(os.getcwd(), str))
        os.rmdir(str)

if __name__ == '__main__':
    creat_folder()
    input('Директории от dir_1 до dir_9 созданы. Нажмите Enter чтобы удалить')
    remove_folder()