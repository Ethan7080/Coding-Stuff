a = 50
b = 10
for i in range(8):
    print(a,end=' ')
    a -= b
    b -= 1

print('\n')
c = 1
d = 1
for i in range(11):
    print(c,end=' ')
    c += d
    d += 1
print('\n')
c = 1
d = 1
print(c,end=' ')
print(d,end=' ')
for i in range(9):
    e = c+d
    print(e,end=' ')
    d = c
    c = e

   


