import random

def rand_list(flist = []):
    if(len(flist) == 0):
        return None
    return random.choice(flist)


if __name__ == '__main__':
    my_list = [1, 2, 3, 4]
    print(rand_list(my_list))
    print(rand_list())