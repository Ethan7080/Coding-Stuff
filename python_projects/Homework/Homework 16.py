while True:
    year = int(input("Input a year: "))
    zodiac = ['Dragon', 'Snake', 'Horse', 'Sheep', 'Monkey', 'Rooster', 'Dog', 'Pig', 'Rat', 'Ox', 'Tiger', 'Hare']
    print("Zodiac is: " + zodiac[year%12-8])
