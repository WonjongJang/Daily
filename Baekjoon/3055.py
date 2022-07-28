import sys
sys.stdin = open('input.txt')
from collections import deque


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(sx, sy):
    q = deque()
    q.append((sx, sy))
    v[sx][sy] = 1

    cnt = 0
    while q:
        for _ in range(len(q)):
            x, y = q.popleft()

            if (x, y) == D:
                return cnt

            if data[x][y] == '*':
                continue

            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if 0 <= nx < R and 0 <= ny < C and (data[nx][ny] == '.' or data[nx][ny] == 'D') and not v[nx][ny]:
                    q.append((nx, ny))
                    v[nx][ny] = 1

        cnt += 1
        water = deque()
        for x in range(R):
            for y in range(C):
                if data[x][y] == '*':
                    for d in range(4):
                        nx = x + dx[d]
                        ny = y + dy[d]
                        if 0 <= nx < R and 0 <= ny < C and data[nx][ny] == '.':
                            water.append((nx, ny))

        while water:
            x, y = water.popleft()
            data[x][y] = '*'

    return 'KAKTUS'

R, C = map(int, input().split())
data = [list(input()) for _ in range(R)]
v = [[0]*C for _ in range(R)]

for i in range(R):
    for j in range(C):
        if data[i][j] == 'S':
            S = (i, j)
        elif data[i][j] == 'D':
            D = (i, j)

print(bfs(S[0], S[1]))