n, k = map(int, input().split())

coinList = []
for i in range(n):
    coinList.append(int(input()))

count = 0
coinList.reverse()

for i in coinList:
    if i <= k:
        count += k // i
        k = k % i
    if k == 0:
        print(count)
        break
