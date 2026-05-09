n = int(input())
grid = []
moning_answer = []
even_answer = []
answer = []
for _ in range(n):
    arr = list(map(int, input().split()))
    grid.append(arr)
# print(grid)

from itertools import combinations
arr1 = list(combinations(range(n), n//2))
# print(arr1)

for i in range(len(arr1)):
    t = arr1[i]
    moning_arr = list(combinations(t, 2))
    # print(arr2)
    even = []
    for j in range(n):
        if j not in t:
            even.append(j)
    # print(even)
    even_arr = list(combinations(even,2))

    moning = 0
    even = 0 
    for k in moning_arr:
        a,b = k
        moning += grid[a][b]
        moning += grid[b][a]
    moning_answer.append(moning)
    for o in even_arr:
        x,y = o
        even += grid[x][y]
        even += grid[y][x]
    even_answer.append(even)

# print(moning_answer)
# print(even_answer)
for p in range(len(moning_answer)):
    answer.append(abs(moning_answer[p]-even_answer[p]))
print(min(answer))
