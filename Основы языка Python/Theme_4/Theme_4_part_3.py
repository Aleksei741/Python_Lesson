

def attack(player, enemy):
    enemy['health'] = enemy['health'] - player['damage']
    return enemy

player1 = {'name': '', 'health': 100, 'damage': 50}
player2 = {'name': '', 'health': 100, 'damage': 50}

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