import sys
sys.stdin = open('input.txt')
from collections import deque


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y, t):
    global ans

    que = deque()
    que.append((x, y, t))
    v[x][y] = 1

    while que:
        x, y, t = que.popleft()

        if t > T:
            return

        if x == N-1 and y == M-1:
            ans = min(ans, t)
            return

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < M and v[nx][ny] == 0:
                if data[nx][ny] == 0:
                    que.append((nx, ny, t+1))
                    v[nx][ny] = 1
                elif data[nx][ny] == 2:
                    tmp = t+1
                    tmp += abs(N-1-nx) + abs(M-1-ny)
                    v[nx][ny] = 1
                    if tmp <= T:
                        ans = tmp

N, M, T = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]

v = [[0]*M for _ in range(N)]
ans = float('inf')
bfs(0, 0, 0)

if ans > T:
    print('Fail')
else:
    print(ans)