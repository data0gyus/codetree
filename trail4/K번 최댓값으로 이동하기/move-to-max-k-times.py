n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())

# Please write your code here.
from collections import deque
r -= 1
c -= 1
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for _ in range(k):
    queue = deque([(r,c)])
    visited = [[False] *n for _ in range(n)]
    visited[r][c] = True
    answer = []
    while queue:
        x,y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <=ny < n:
                if not visited[nx][ny] and grid[r][c] > grid[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx,ny))
                    answer.append((grid[nx][ny], nx, ny))

    # print(answer)

    if answer == []:
        break
    
    temp = 0 
    dist = []
    for t,x,y in answer:
        # print(t,x,y)
        if temp < t:
            dist = []
            temp = t
            dist.append((x,y))
        elif temp == t:
            dist.append((x,y))

    # print(dist)
    # print(temp)
    r,c = min(dist)
    # print(r,c)

print(r+1, c+1)


