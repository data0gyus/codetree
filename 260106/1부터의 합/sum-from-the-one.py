n = int(input())
total = 0

for i in range(101):
    total += i
    if total >= n:
        print(i)
        break

