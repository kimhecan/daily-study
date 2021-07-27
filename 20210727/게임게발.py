n, m = map(int, input().split())
a, b, direction = map(int, input().split())
matrix = [list(map(int, input())) for _ in range(n)]
d = [[0]*m for _ in range(n)]
d[a][b] = 1

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]


def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


count = 1
turn_time = 0

while True:
    turn_left()
    nx = a + dx[direction]
    ny = b + dy[direction]
    if d[nx][ny] == 0 and matrix[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1

    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        if matrix[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0
