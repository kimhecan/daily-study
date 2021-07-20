import sys

cityNum = int(input())
distances = list(map(int, sys.stdin.readline().split()))
oilPrices = list(map(int, sys.stdin.readline().split()))

result = 0
minCost = oilPrices[0]

for i in range(cityNum-1):
    if oilPrices[i] < minCost:
        minCost = oilPrices[i]
    result += minCost * distances[i]
    print(result, 'result')

print(result)
