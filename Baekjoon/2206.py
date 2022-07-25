import sys
sys.stdin = open('input.txt')
from collections import deque


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y, b):
    global min_v

    q = deque()
    q.append([x, y, b])
    v[x][y][b] = 1

    while q:
        x, y, b = q.popleft()

        if x == N-1 and y == M-1:
            return v[x][y][b]

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < M and not v[nx][ny][b]:
                if data[nx][ny] and b:
                    q.append([nx, ny, b-1])
                    v[nx][ny][b-1] = v[x][y][b] + 1
                elif not data[nx][ny]:
                    q.append([nx, ny, b])
                    v[nx][ny][b] = v[x][y][b] + 1
    return -1


N, M = map(int, input().split())
data = [list(map(int, input())) for _ in range(N)]

v = [[[0] * 2 for _ in range(M)] for _ in range(N)]

print(bfs(0, 0, 1))