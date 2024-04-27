a = eval(int(input('Give me numbers plz: ')))
if type(a) == list:
   lis = []
   num = a
   x = a
   total = 0
   count_of_digits = 0
   while x > 0:
      x = x//10
      count_of_digits += 1
   while num != 0:
       lis.append(num % 10)
       num //= 10
   lis.reverse()
   for i in range(count_of_digits):
       if i == 4:
           total += lis[i]
           print(str(lis[i]) + ' = ' + str(total),end='\n')
           break
       if i % 2 == 0:
           total += lis[i] - lis[i+1]
           print(str(lis[i]) + ' -',end=' ')
       else:
           total += lis[i] + lis[i+1]
           print(str(lis[i]) + ' +',end=' ')
       
   print('The total is ' + str(total))
else:
   print('not anumber')

