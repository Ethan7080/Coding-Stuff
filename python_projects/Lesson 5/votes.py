import random
vote = [0, 0, 0, 0]
avengers = ["IronMan", "CaptainAmerica", "Hulk", "SpiderMan"]
for i in range(1000):
    votes = random.randint(0, 3)
    vote[votes] += 1
for 王予安 in range(4):
    print(avengers[王予安],'Votes:', vote[王予安])
    
