lst = [1, 2, 2, 3, 4, 5, 5]
print(lst)
for i in range(len(lst) - 1, -1, -1):
    if lst[i] == 2 or lst[i] == 5:
        lst.pop(i)
print(lst)
