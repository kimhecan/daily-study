from collections import deque

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(ripes):
    queue = deque(ripes)
    day = -1
    while queue:
        day += 1
        for _ in range(len(queue)):
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx, ny))

    for i in graph:
        if 0 in i:
            return -1

    return day


ripes = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            ripes.append((i, j))

print(bfs(ripes))
