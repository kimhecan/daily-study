from sys import stdin
from collections import deque

n = int(input())

matrix = [stdin.readline().rstrip() for _ in range(n)]
visited = [[0]*n for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

cntList = []


def bfs(x, y):
    cnt = 1
    q = deque()
    q.append((x, y))
    visited[x][y] = 1

    while q:
        x, y = q.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                if matrix[nx][ny] == "1" and visited[nx][ny] == 0:
                    cnt += 1
                    q.append((nx, ny))
                    visited[nx][ny] = 1

    return cnt


for i in range(n):
    for j in range(n):
        if matrix[i][j] == "1" and visited[i][j] == 0:
            cntList.append(bfs(i, j))

print(len(cntList))

for i in sorted(cntList):
    print(i)
