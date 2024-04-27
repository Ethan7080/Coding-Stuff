a = 0
b = 1
pre_number = 0
number_now = 1


for i in range(23):
    number_now = number_now + pre_number
    pre_number = number_now - pre_number
    print(number_now)
print('共'+str(number_now*2)+'只兔子')
