n = int(input())

points = []
for i in range(n):
    points.append(int(input()))

points.reverse()
count = 0
for i in range(1, n):
    while points[i] >= points[i-1]:
        points[i] = points[i] - 1
        count += 1

print(count)
