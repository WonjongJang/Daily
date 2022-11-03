import sys
sys.stdin = open('input.txt')

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    que = []
    que.append((x, y))
    v[x][y] = 1

    while que:
        x, y = que.pop(0)
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < N and data[nx][ny] > h and not v[nx][ny]:
                que.append((nx, ny))
                v[nx][ny] = 1

N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]

max_v = 0
for h in range(101):
    v = [[0]*N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if data[i][j] > h and not v[i][j]:
                bfs(i, j)
                cnt += 1

    if not cnt:
        break

    max_v = max(max_v, cnt)

print(max_v)