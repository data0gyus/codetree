arr = []

for _ in range(10):
    num = int(input())
    arr.append(num)

a = 0
b = 0
for i in arr:
    if i % 3 == 0:
        a += 1
    if i % 5 == 0:
        b += 1 
print(a , b )