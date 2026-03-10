import sys
input = sys.stdin.readline

n,m = map(int, input().split())
list1 = [list(map(int,input().split())) for _ in range(m)]
list2 = [list(map(int,input().split())) for _ in range(m)]

for i in range(n):
    for j in range(m):
        print(1 if list1[i][j] != list2[i][j] else 0, end=" ")
    print()