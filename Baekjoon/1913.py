import sys
sys.stdin = open('input.txt')


dx = [1, 0, -1, 0]  # 하우상좌
dy = [0, 1, 0, -1]


N = int(input())
F = int(input())

table = [[0]*N for _ in range(N)]

x, y, n, d = 0, 0, N**2, 0
fx, fy = 0, 0
while True:
    table[x][y] = n

    if n == F:
        fx, fy = x, y

    if n == 1:
        break

    nx = x + dx[d]
    ny = y + dy[d]
    if 0 <= nx < N and 0 <= ny < N and not table[nx][ny]:
        x, y = nx, ny
        n -= 1
    else:
        d = (d+1) % 4

for t in table:
    print(*t)
print(fx+1, fy+1)
