while True:
    i = 1
    a = int(input())
    while i <= 1000:
        temp = i
        if temp % a == 0:
            print(temp,end=' ')
        else:
            while temp != 0:
                if temp % 10 == a:
                    print(i,end=' ')
                    break
                temp //= 10
        i += 1
    print
        
