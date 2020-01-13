from player import Player
from hamster import Hamster


class Game():
    map = []
    hamsters = []
    number_hamster = 4
    game_on = True
    directions = {'w': 's', 's': 'w', 'a': 'd', 'd': 'a'}

    def __init__(self):
        self.create_object()

    def create_object(self):
        self.player = Player()
        self.hamsters = []
        position = []
        position.append(self.player.position_init())
        for i in range(self.number_hamster):
            self.hamsters.append(Hamster(i))
        for i in self.hamsters:
            position.append(i.position_init(position))

    def output_on_display(self, id=''):
        self.object_to_map()
        print('|{:>10}|{:>10}|{:>10}|'.format('', 'Player', 'Target'))
        if id in [0, 1, 2, 3]:
            print('|{:>10}|{:>10}|{:>10}|'.format('Health', self.player.r_health(), self.hamsters[id].r_health()))
            print('|{:>10}|{:>10}|{:>10}|'.format('Damage', self.player.r_damage(), self.hamsters[id].r_damage()))
        else:
            print('|{:>10}|{:>10}|{:>10}|'.format('Health', self.player.r_health(), '-'))
            print('|{:>10}|{:>10}|{:>10}|'.format('Damage', self.player.r_damage(), '-'))
        for i in range(4):
            print('     ', end='')
            for j in range(4):
                print('| {} |'.format(self.map[i][j]), end='')
            print()

    def object_to_map(self):
        self.map = [['*', '*', '*', '*'],
                    ['*', '*', '*', '*'],
                    ['*', '*', '*', '*'],
                    ['*', '*', '*', '*']]
        self.map[self.player.x][self.player.y] = 'x'
        if self.hamsters:
            for i in range(len(self.hamsters)):
                self.map[self.hamsters[i].x][self.hamsters[i].y] = '{}'.format(self.hamsters[i].return_hid())

    def game_process(self, destination):
        ''' destination = w, a, s, d'''
        if destination == 's':
            self.player.Down()
        if destination == 'w':
            self.player.Up()
        if destination == 'a':
            self.player.Left()
        if destination == 'd':
            self.player.Right()
        if destination == 'q':
            game_on = False
        if destination == 'e':
            self.player.self_heal()

        id = None
        for i in range(len(self.hamsters)):
            if self.player.position() == self.hamsters[i].position():
                id = i
                break

        if id in [0, 1, 2, 3]:
            self.player.was_hit(self.hamsters[id].r_damage())
            self.hamsters[id].was_hit(self.player.r_damage())
            if self.hamsters[id].r_health() <= 0:
                self.hamsters.pop(id);
                self.output_on_display()
            else:
                if destination == 's':
                    self.player.Up()
                if destination == 'w':
                    self.player.Down()
                if destination == 'a':
                    self.player.Right()
                if destination == 'd':
                    self.player.Left()
                self.output_on_display(id)
        else:
            self.output_on_display()

        if self.player.r_health() <= 0:
            print('game over')
            self.game_on = False
        if len(self.hamsters) == 0:
            print('victory')
            self.game_on = False




    def strat(self):
        self.output_on_display()
        while self.game_on:
            command = input('Insert command: ')
            if command in ['a', 's', 'd', 'w', 'e', 'q']:
                self.game_process(command)



game = Game()

game.strat()
