total = 0

for _ in range(4):
    list1 = list(map(int, input().split()))
    for i in list1:
        if i % 5 == 0:
            total +=1 
print(total)