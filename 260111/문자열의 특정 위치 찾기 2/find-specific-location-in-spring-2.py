arr = ["apple","banana","grape","blueberry","orange"]

a = input()

cnt = 0
for str in arr:
    if str[2] == a or str[3] == a:
        print(str)
        cnt += 1
print(cnt)