import sys
sys.stdin = open('input.txt')
from collections import deque


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def check():
    for x in range(N):
        for y in range(M):
            if v[x][y] == 0:
                return 0
    return 1

M, N = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]

v = [[0] * M for _ in range(N)]

que = deque()
for x in range(N):
    for y in range(M):
        if data[x][y] == 1:
            que.append((x, y))
            v[x][y] = 1
        if data[x][y] == -1:
            v[x][y] = 1

day = 0
while True:
    for i in range(len(que)):
        x, y = que.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < M and not v[nx][ny] and data[nx][ny] == 0:
                que.append((nx, ny))
                v[nx][ny] = 1

    if not que:
        break

    day += 1

if check():
    print(day)
else:
    print(-1)


