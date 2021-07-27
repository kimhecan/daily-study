n, m = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]

minlist = []

for i in matrix:
    minlist.append(min(i))


print(max(minlist))
