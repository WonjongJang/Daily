import sys
sys.stdin = open('input.txt')
from collections import deque
input = sys.stdin.readline


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
hx = [-1, -2, -2, -1, 1, 2, 2, 1]
hy = [-2, -1, 1, 2, -2, -1, 1, 2]

def bfs(s, k, cnt):
    q = deque()
    q.append((s, s, k, cnt))
    v[s][s][k] = 1

    while q:
        x, y, k, cnt = q.popleft()
        # print(x, y, k, cnt)

        if x == H-1 and y == W-1:
            return cnt

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < H and 0 <= ny < W and not v[nx][ny][k] and not data[nx][ny]:
                q.append((nx, ny, k, cnt+1))
                v[nx][ny][k] = 1

        if k > 0:
            for d in range(8):
                nx = x + hx[d]
                ny = y + hy[d]
                if 0 <= nx < H and 0 <= ny < W and not v[nx][ny][k-1] and not data[nx][ny]:
                    q.append((nx, ny, k-1, cnt+1))
                    v[nx][ny][k-1] = 1
    return -1

K = int(input())
W, H = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(H)]

v = [[[0]*(K+1) for _ in range(W)] for _ in range(H)]
ans = bfs(0, K, 0)

print(ans)