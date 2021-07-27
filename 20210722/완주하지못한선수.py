def solution(participant, completion):
    dic = {}
    for i in participant:
        if dic.get(i) != None:
            dic[i] += 1
        else:
            dic[i] = 1

    for i in completion:
        dic[i] -= 1
    for i in list(dic.keys()):
        if dic[i] != 0:
            return i


print(solution(["mislav", "stanko", "mislav", "ana"],
               ["stanko", "ana", "mislav"]))


# def solution(participant, completion):
#     answer = ''
#     temp = 0
#     dic = {}
#     for part in participant:
#         dic[hash(part)] = part
#         temp += int(hash(part))
#     for com in completion:
#         temp -= hash(com)
#     answer = dic[temp]

#     return answer
