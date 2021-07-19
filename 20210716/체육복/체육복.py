def solution(n, lost, reserve):
    n -= len(lost)

    for i in lost:
        for j in reserve:
            if i == j:
                lost = list(filter(lambda x: x != i, lost))
                reserve = list(filter(lambda x: x != j, reserve))
                n += 1

    for i in lost:
        for j in reserve:
            if i - 1 == j or i+1 == j:
                reserve = list(filter(lambda x: x != j, reserve))
                n += 1
                break

    return n


print(solution(	6, [2, 4, 6], [1, 3, 5, 6]))
