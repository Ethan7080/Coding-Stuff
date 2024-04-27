import random

lucky_num = random.randint(1, 100)
Bingo = False
trys = int(input('Enter how many trys you need:'))
while Bingo == False:
    print('Trys left: ' + str(trys))
    guess_num = int(input("Plz enter a number:"))

    if guess_num == lucky_num:
        print('Bingo')
        Bingo = True
        break
    elif guess_num > lucky_num:
        print('Too big')

    else:
        print('Too small')

    if trys == 1:
        print('You have no more Trys')
        print('The answer was: ' + str(lucky_num))
        print('GAMEOVER')
        break
    trys -= 1
