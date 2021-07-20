s = int(input())

for i in range(1, 99999999):
    if i*(i+1) / 2 > s:
        print(i-1)
        break
