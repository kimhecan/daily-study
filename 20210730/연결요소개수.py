import sys
from collections import deque

nodeNum, edgeNum = map(int, sys.stdin.readline().rstrip().split())
visited = []
graph = {}

for i in range(nodeNum):
    graph[i+1] = []

for i in range(edgeNum):
    start, end = map(int, sys.stdin.readline().rstrip().split())
    graph[start].append(end)
    graph[end].append(start)


count = 0


def bfs(graph, node):
    queue = deque()
    queue.append(node)
    visited.append(node)
    while queue:
        node = queue.popleft()
        for x in graph[node]:
            if x not in visited:
                queue.append(x)
                visited.append(x)


for i in range(1, nodeNum + 1):
    if i not in visited:
        bfs(graph, i)
        count += 1

print(count)
