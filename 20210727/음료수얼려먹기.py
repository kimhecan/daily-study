from collections import deque

n, m = map(int, input().split())

# matrix = [list(map(int, input())) for _ in range(n)]
matrix = [list(map(int, input())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]


def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if matrix[x][y] == 0:
        matrix[x][y] = 1
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False


result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)
