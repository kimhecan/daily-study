n = int(input())

d = [n+1] * (n+1)
d[0] = 0


for i in [3, 5]:
    for j in range(i, n+1):
        if d[j-i] != n:
            d[j] = min(d[j], d[j-i] + 1)

if d[n] == n+1:
    print(-1)
else:
    print(d[n])
