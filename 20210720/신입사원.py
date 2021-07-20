import sys

testNum = int(input())
resultList = []

for i in range(testNum):
    cnt = 1
    caseNum = int(input())
    caseList = []
    for j in range(caseNum):
        a, b = map(int, sys.stdin.readline().split())
        caseList.append([a, b])

    caseList.sort()
    maxRank = caseList[0][1]

    for i in range(1, caseNum):
        if maxRank > caseList[i][1]:
            cnt += 1
            maxRank = caseList[i][1]

    resultList.append(cnt)

for i in resultList:
    print(i)
