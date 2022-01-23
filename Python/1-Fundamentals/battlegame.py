human = "Human"
human_hp = 150
human_damage = 20

elf = "Elf"
elf_hp = 100
elf_damage = 100

wizard = "Wizard"
wizard_hp = 70
wizard_damage = 150

# dragon = "Dragon"
dragon_hp = 300
dragon_damage = 30

while True:
    print('1) ' + human)
    print('2) ' + elf)
    print('3) ' + wizard)
    character = input('Choose your character: ')
    if character == '1':
        character = human
        my_hp = human_hp
        my_damage = human_damage
    elif character == '2':
        character = elf
        my_hp = elf_hp
        my_damage = elf_damage
    elif character == '3':
        character = wizard
        my_hp = wizard_hp
        my_damage = wizard_damage
    else:
        print('Unknown character')
    print('You chose ' + character)
    print('Your HP: ' + str(my_hp))
    print('Your damage: ' + str(my_damage))
    break

while True:
    dragon_hp = dragon_hp - my_damage
    print('The ' + character + ' damaged the Dragon')
    print("The Dragon's hitpoints are now: " + str(dragon_hp))
    print("\n")
    if dragon_hp <= 0:
        print('The Dragon has lost the battle')
        break

    my_hp = my_hp - dragon_damage
    print('The Dragon strikes back at' + character)
    print("The " + character + "'s hitpoints" + str(my_hp))
    print("\n")
    if my_hp <= 0:
        print('The ' + character + ' has lost the battle')
        break
