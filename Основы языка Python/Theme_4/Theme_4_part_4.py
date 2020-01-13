

def attack(player, enemy):
    enemy['health'] = enemy['health'] - damage(player['damage'], player['armor'])
    return enemy

def damage(damage, armor):
    return damage / armor

player1 = {'name': '', 'health': 100, 'damage': 50, 'armor': 1.2}
player2 = {'name': '', 'health': 100, 'damage': 50, 'armor': 1.2}

player1['name'] = input('Введите имя первого игрока: ')
#player1['name'] = 'p1'

player2['name'] = input('Введите имя второго игрока: ')
#player2['name'] = 'p2'

print(player1)
print(player2)

print('{} атакует {}'.format(player1['name'], player2['name']))
player2 = attack(player1, player2)

print(player1)
print(player2)