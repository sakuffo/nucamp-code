import random

high_score = 0


def dice_game():
    global high_score
    while True:
        print('Current High Score: ' + str(high_score))
        print('1) Roll Dice')
        print('2) Leave Game')
        choice = input('Enter your choice: ')
        if choice == '1':
            dice_1 = random.randint(1, 6)
            dice_2 = random.randint(1, 6)
            print('You roll a...' + str(dice_1))
            print('You roll a...' + str(dice_2))
            total = dice_1 + dice_2
            print('Your total is: ' + str(total))
            if total > high_score:
                high_score = total
                print('New High Score!\n')
        elif choice == '2':
            print('Goodbye!')
            break


dice_game()
