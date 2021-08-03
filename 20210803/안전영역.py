from collections import deque

# 높이는 1이상 100이하

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y, h, visited):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and h < graph[nx][ny] and visited[nx][ny] == 0:
                queue.append((nx, ny))
                visited[nx][ny] = 1


counts = []
for h in range(0, 101):
    visited = [[0]*n for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] > h and visited[i][j] == 0:
                bfs(i, j, h, visited)
                count += 1

    counts.append(count)

print(counts)
print(max(counts))
