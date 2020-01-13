from Object import Object
import random

class Player(Object):

    def __init__(self):
        self.health = 11
        self.damage = 1

    def __str__(self):
        return 'x'

    def self_heal(self):
        if self.health < 10:
            self.health += 1
        return self.health


