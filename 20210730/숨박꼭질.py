from collections import deque

n, k = map(int, input().split())
line = [0]*100001
visited = [0]*100001
visited[n] = 1


def bfs(line, x):
    queue = deque()
    queue.append(x)
    visited[x] = 1
    while queue:
        x = queue.popleft()
        for i in [x-1, x+1, x*2]:
            if 0 <= i < 100001 and visited[i] == 0:
                visited[i] = 1
                line[i] = line[x] + 1
                queue.append(i)
                if i == k:
                    return


bfs(line, n)
print(line[k])
