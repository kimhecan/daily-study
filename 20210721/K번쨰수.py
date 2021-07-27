def solution(array, commands):
    answer = []
    for command in commands:
        filtereds = sorted(array[command[0]-1:command[1]])
        answer.append(filtereds[command[2]-1])
    return answer
