from gameworld import GameWorld


rps_game = GameWorld()
P1 = rps_game.player
PE = rps_game.enemy

while True:
    print('Welcome to rock paper scissors')
    weapon = P1.attack()
    enemy_weapon = PE.attack(rps_game.weapons.values())
    defeated_weapon = rps_game.weapons[weapon]
    if weapon == enemy_weapon:
        print(f'This round is a draw! {weapon} are {enemy_weapon} matched')
    elif enemy_weapon in defeated_weapon:
        print(f'The player has triumphed! {weapon} beats {enemy_weapon}!')
    else:
        print(f'The enemy has won! {enemy_weapon} beats {weapon}')

    option = input('(Y) to play again and anything else to exit: ').lower()
    if option != 'y':
        break
