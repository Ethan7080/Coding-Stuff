import random
n1, n2, n3, n4, n5, n6 = 0, 0, 0, 0, 0, 0
for i in range(100):
    rand = random.randint(1, 6)
    if rand == 1:
        n1 += 1
    elif rand == 2:
        n2 += 1
    elif rand == 3:
        n3 += 1
    elif rand == 4:
        n4 += 1
    elif rand == 5:
        n5 += 1
    else:
        n6 += 1

print(n1, n2, n3, n4, n5, n6)
