import random
mon = ['m0','m1','m2','m3','m4','m5']
while len(mon) != 0:
    a = random.choice(mon)
    print(a)
    mon.remove(a)
    
