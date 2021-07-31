import sys
from collections import deque

n = int(input())
graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = []


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1
    count = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1 and visited[nx][ny] == 0:
                queue.append((nx, ny))
                visited[nx][ny] = 1
                count += 1

    return count


for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and visited[i][j] == 0:
            result.append(bfs(i, j))

result.sort()
print(len(result))
for i in result:
    print(i)
