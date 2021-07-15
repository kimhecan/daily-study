def atm(num, times):
    sortedTimes = sorted(times)
    total = 0
    result = 0

    for value in sortedTimes:
        total += value
        result += total

    return result


print(atm(5, [3, 1, 4, 3, 2]))

# n = int(input())
# arr = list(map(int, sys.stdin.readline().split()))
