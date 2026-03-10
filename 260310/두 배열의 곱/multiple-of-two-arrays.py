import sys
input = sys.stdin.readline

list1 = [list(map(int, input().split())) for _ in range(3)]
a = input()
list2 = [list(map(int, input().split())) for _ in range(3)]

stack=[]
for i in range(3):
    row = []
    for j in range(3):
        row.append(list1[i][j] * list2[i][j])
    stack.append(row)

for k in range(3):
    print(*stack[k])