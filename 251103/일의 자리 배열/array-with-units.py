a = list(map(int, input().split()))

for i in range(2,10):
    b = a[i-2] + a[i-1]
    a.append(b)

total = [x%10 for x in a]

for i in range(len(total)):
    print(total[i], end=" ")