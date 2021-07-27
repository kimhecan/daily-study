position = input()
x = int(ord(position[0])) - int(ord('a')) + 1
y = int(position[1])

dx, dy = [1, -1, 2, 2, 1, -1, -2, 2], [2, 2, -1, 1, -2, -2, 1, -1]

count = 0

for i in range(8):
    tempx = x + dx[i]
    tempy = y + dy[i]
    if 1 <= tempx <= 8 and 1 <= tempy <= 8:

        count += 1

print(count)
