a = int(input())
b = int(input())
c = min(a, b)
while c > 0:
    if a % c == 0 and b % c == 0:
        print(c)
        break
    c -= 1
print(c)
