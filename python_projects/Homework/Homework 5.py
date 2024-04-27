
while True:
    a = int(input('Score:'))
    scr = ' '
    if a > 950:
        scr = 'A+'

    elif a > 850 and a < 949:
        scr = 'A'

    elif a > 750 and a < 849:
        scr = 'B+'

    elif a > 600 and a < 749:
        scr = 'C'
        
    else:
        scr = 'F'

    print(scr)
    a +=1
