import sys
sys.stdin = open('input.txt')


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    que = []
    que.append((x, y))
    data[x][y] = 2
    while que:
        x, y = que.pop(0)
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < M and 0 <= ny < N and data[nx][ny] == 1:
                que.append((nx, ny))
                data[nx][ny] = 2

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())

    data = [[0]*N for _ in range(M)]

    for _ in range(K):
        x, y = map(int, input().split())
        data[x][y] = 1

    ans = 0
    for i in range(M):
        for j in range(N):
            if data[i][j] == 1:
                bfs(i, j)
                ans += 1

    print(ans)