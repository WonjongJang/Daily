import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10**6)


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def recur(x, y, color):
    v[x][y] = 1

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < N and 0 <= ny < N and not v[nx][ny] and data[nx][ny] == color:
            recur(nx, ny, color)

N = int(input())
data = [list(input()) for _ in range(N)]

v = [[0] * N for _ in range(N)]
cnt = 0
for i in range(N):
    for j in range(N):
        if not v[i][j]:
            cnt += 1
            recur(i, j, data[i][j])

for i in range(N):
    for j in range(N):
        if data[i][j] == "G":
            data[i][j] = "R"

v = [[0] * N for _ in range(N)]
cnt_d = 0
for i in range(N):
    for j in range(N):
        if not v[i][j]:
            cnt_d += 1
            recur(i, j, data[i][j])


print(cnt, cnt_d)