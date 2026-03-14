total = 0
for i in range(4): 
    list1 = list(map(int, input().split()))
    for k in range(i+1):
        total += list1[k]
print(total)