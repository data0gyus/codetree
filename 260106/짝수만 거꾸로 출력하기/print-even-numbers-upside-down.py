n = int(input())
arr = list(map(int, input().split()))
stack = []

for i in reversed(arr):
    if i % 2 ==0:
        print(i, end=" ")