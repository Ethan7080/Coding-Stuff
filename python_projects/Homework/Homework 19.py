while True:
    s_num = int(input())
    l_num = int(input())
    f_num = int(input())
    makebrick = True
    if f_num <= s_num or (f_num % 5 == 0 and f_num // 5 <= l_num):
        print(makebrick)
    elif f_num > s_num:
        if f_num // 5 <= l_num and f_num % 5 <= s_num:
            print(makebrick)
        elif f_num // 5 > l_num and (f_num - 5*l_num) <= s_num:
            print(makebrick)
        else:
            makebrick = False
            print(makebrick)
    else:
        makebrick = False
        print(makebrick)
