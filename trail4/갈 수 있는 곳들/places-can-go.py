n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
points = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.
from collections import deque

visited = [[False]*n for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
queue = deque()
for x,y in points:
    visited[x-1][y-1] = True
    queue.append((x-1,y-1))

# print(queue)
# print(visited)
while queue:
    x,y = queue.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx< n and 0<= ny < n :
            if not visited[nx][ny] and grid[nx][ny] == 0:
                visited[nx][ny] = True
                queue.append((nx,ny))

cnt = 0
for i in range(len(visited)):
    for j in range(len(visited[0])):
        if visited[i][j] == True:
            cnt +=1
print(cnt)