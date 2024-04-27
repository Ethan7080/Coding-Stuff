import random
n0 = 0
n1 = 0
for i in range(1000):
    rand = random.randint(0,1)
    if rand == 0:
        n0 += 1

    else:
        n1 += 1


print(n0,n1)
print(n0/(n1 + n0))
    
