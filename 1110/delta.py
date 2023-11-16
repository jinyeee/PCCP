x, y = 1, 1

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for d in range(4):
    nx = x + dx[d]
    ny = y + dy[d]
    print(nx, ny)