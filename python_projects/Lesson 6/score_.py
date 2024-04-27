import random
score = []
total = 0
low = 0
p = 100
for i in range(p):
    a = random.randint(45, 100)
    score.append(a)
    total += a
    if a <= 60:
        low += 1
print(score)
print("总分: " + str(total))
print('不及格率: ' + str(low / p))
