import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def recur(x, y):
    if x == M-1 and y == N-1:
        return 1

    if dp[x][y] == -1:
        dp[x][y] = 0

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < M and 0 <= ny < N and data[x][y] > data[nx][ny]:
                dp[x][y] += recur(nx, ny)

    return dp[x][y]

M, N = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(M)]
dp = [[-1]*N for _ in range(M)]

print(recur(0, 0))