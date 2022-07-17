import sys
sys.stdin = open('input.txt')
from collections import deque


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    global cnt

    q = deque()
    q.append((x, y))
    arr[x][y] = 2
    cnt += 1
    while q:
        x, y = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 1:
                arr[nx][ny] = 2
                cnt += 1
                q.append((nx, ny))


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

tot = []
for i in range(N):
    for j in range(M):
        cnt = 0
        if arr[i][j] == 1:
            bfs(i, j)
            tot.append(cnt)

if tot:
    print(len(tot))
    print(max(tot))
else:
    print(0)
    print(0)