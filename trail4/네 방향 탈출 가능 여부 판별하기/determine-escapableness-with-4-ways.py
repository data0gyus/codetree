n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
from collections import deque

visited = [[False]*m for _ in range(n)]
dx = [-1,1, 0,0]
dy = [0,0,-1,1]

queue = deque([(0,0)])
visited[0][0] = True

result = 0 

while queue:
    x,y = queue.popleft()

    if x == n-1 and y == m-1:
        result = 1
        break
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if not visited[nx][ny] and a[nx][ny] == 1:
                visited[nx][ny] = True
                queue.append((nx,ny))

print(result)