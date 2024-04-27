a = '^^^^^'
b = '#'
c = ''
loop = 10
for i in range(11):
    for i in range(loop):
        b += "#"
    print(c + b + a + b)
    loop -= 1
    b = '#'
    c += ' '
    
