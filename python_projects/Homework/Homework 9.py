
a = input()
b = input()
c = input()
d = input()
e = input()
f = input()
g = input()
h = input()
if a > b:
    big_num = a
else:
    big_num = b
if big_num <= c:
    big_num = c
if big_num <= d:
    big_num = d
if big_num <= e:
    big_num = e 
if big_num <= f:
    big_num = f
if big_num <= g:
    big_num = g
if big_num <= h:
    big_num = h
if a < b:
    small_num = a
else:
    small_num = b
if small_num >= c:
    small_num = c
if small_num >= d:
    small_num = d
if small_num >= e:
    small_num = e 
if small_num >= f:
    small_num = f
if small_num >= g:
    small_num = g
if small_num >= h:
    small_num = h
average = (int(a) + int(b) + int(c) + int(d) + int(e) + int(f) + int(g) + int(h)) / 8
print('The BIGGEST number is...' + big_num + '!\nThe smallest number is...' + small_num + '!')
print('The average is...')
print(round(average, 2))



