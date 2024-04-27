while True:
    eggs = int(input('Enter a number of eggs: '))
    cartons = eggs // 12
    if eggs % 12 != 0:
        cartons += 1
    print(int(cartons))
