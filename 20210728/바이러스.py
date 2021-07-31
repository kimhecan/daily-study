from collections import deque

nodeNum = int(input())
edgeNum = int(input())
graph = {}

for i in range(nodeNum):
    graph[i+1] = []

for i in range(edgeNum):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

for i in range(nodeNum):
    graph[i+1].sort()


def bfs(visited, graph, node):
    queue = deque()
    queue.append(node)
    visited.append(node)
    count = 0
    while queue:
        s = queue.popleft()
        for node in graph[s]:
            if node not in visited:
                visited.append(node)
                queue.append(node)
                count += 1

    return count


print(bfs([], graph, 1))
