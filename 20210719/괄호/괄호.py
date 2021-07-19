expression = input().split(sep='-')
total = 0
for idx, value in enumerate(expression):
    if idx == 0:
        total += sum(list(map(int, value.split(sep='+'))))
    else:
        total -= sum(list(map(int, value.split(sep='+'))))
print(total)
