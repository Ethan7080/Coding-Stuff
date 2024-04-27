import random
gold = []
for i in range(10):
    gold.append(random.randint(10, 100))
print('之前，Before: ' + str(gold))
for i in range(10):
    gold[i] -= 15
    if gold[i] < 0:
        gold[i] = 0
print('现在，Now: ' + str(gold))


