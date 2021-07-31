from collections import deque

testCase = int(input())
countList = []
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1 and visited[nx][ny] == 0:
                queue.append((nx, ny))
                visited[nx][ny] = 1


for _ in range(testCase):
    m, n, k = map(int, input().split())
    graph = [[0]*m for _ in range(n)]
    visited = [[0]*m for _ in range(n)]

    count = 0
    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1 and visited[i][j] == 0:
                bfs(i, j)
                count += 1

    countList.append(count)


for i in countList:
    print(i)
