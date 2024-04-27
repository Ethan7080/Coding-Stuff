while True:
    num = int(input('Plz enter an integer: '))
    while num != 0:
        print(num % 100,end=' ')
        num //= 100
    print('\n')


