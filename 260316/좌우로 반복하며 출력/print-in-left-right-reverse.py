n = int(input())

for i in range(n):
    row = []
    cnt = 1
    for j in range(n):
        row.append(cnt)
        cnt += 1
    if i % 2 !=0:
        row.reverse()
    for j in range(n):
        print(row[j], end="")
    print()
