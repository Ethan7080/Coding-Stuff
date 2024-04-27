nums = []
for i in range(3):
    nums.append(input())
for i in nums:
    for j in nums:
        for k in nums:
            if (i != j and j != k and i != k):
                print(str(i), str(j), str(k))























