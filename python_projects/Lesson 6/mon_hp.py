import random
monster_hp = []
for i in range(5):
    monster_hp.append(random.randint(1, 5))           
for i in range(5):
    monster_hp[i] -= 1
    if monster_hp[i] == 0:
        monster_hp[i] = 'dead'
print(monster_hp)
      

