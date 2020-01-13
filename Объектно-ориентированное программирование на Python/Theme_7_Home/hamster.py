from Object import Object
import random


class Hamster(Object):
    hid = 0

    def __init__(self, hid):
        self.health = random.randint(1, hid+1)
        self.damage = random.randint(1, hid+1)
        self.armor = random.randint(1, hid+1)
        self.hid = hid


    def __str__(self):
        return str(self.hid)

    def return_hid(self):
        return self.hid

