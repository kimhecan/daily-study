def solution(left, right):
    total = 0
    for i in range(left, right+1):
        cnt = 0
        for j in range(1, i//2):
            if i % j == 0:
                if (i // j == j):
                    cnt += 1
                else:
                    cnt += 2

        if cnt % 2 == 0:
            total += i
        else:
            total -= i

    return total


print(solution(1, 1))


# def solution(left, right):
#     answer = 0
#     for i in range(left,right+1):
#         if int(i**0.5)==i**0.5:
#             answer -= i
#         else:
#             answer += i
#     return answer
