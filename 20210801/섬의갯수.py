import sys
from collections import deque


w, h = map(int, input().split())
result = []
dx = [0,  0, 1, -1, 1, 1, -1, -1]
dy = [-1, 1, 0,  0, -1, 1, 1, -1]


def bfs(x, y, graph, visited):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1

    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] == 1 and visited[nx][ny] == 0:
                queue.append((nx, ny))
                visited[nx][ny] = 1


while w != 0 or h != 0:
    graph = [list(map(int, sys.stdin.readline().rstrip().split()))
             for _ in range(h)]
    visited = [[0]*w for _ in range(h)]
    count = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1 and visited[i][j] == 0:
                bfs(i, j, graph, visited)
                count += 1
    result.append(count)
    w, h = map(int, input().split())


for i in result:
    print(i)
