import random

lucky_num = random.randint(1, 1000)
Bingo = False
trys = 20
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
