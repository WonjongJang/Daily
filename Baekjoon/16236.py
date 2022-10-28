import sys
sys.stdin = open('input.txt')


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y, size):
    v = [[-1]*N for _ in range(N)]

    que = [(x, y)]
    v[x][y] = 0
    tmp = []
    while que:
        x, y = que.pop(0)
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < N and v[nx][ny] == -1 and data[nx][ny] <= size:
                que.append((nx, ny))
                v[nx][ny] = v[x][y] + 1
                if 0 < data[nx][ny] < size:
                    tmp.append((nx, ny, v[nx][ny]))

    return sorted(tmp, key=lambda t: (-t[2], -t[0], -t[1]))

N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]

x, y, size = 0, 0, 2
for i in range(N):
    for j in range(N):
       if data[i][j] == 9:
           x = i
           y = j

cnt = 0
ans = 0
while True:
    data[x][y] = 0
    posi = bfs(x, y, size)

    if len(posi) == 0:
        break

    nx, ny, d = posi.pop()

    ans += d
    x, y = nx, ny
    cnt += 1
    if cnt == size:
        size += 1
        cnt = 0

print(ans)