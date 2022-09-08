import sys
sys.stdin = open('input.txt')
from collections import deque


def bfs(x):
    que = deque()
    que.append(x)
    v[x] = 1

    while que:
        x = que.popleft()

        for d in range(8):
            if d < 6:
                nx = x + dx[d]
                if 0 <= nx <= 100000 and not v[nx]:
                    que.append(nx)
                    v[nx] = v[x]+1
            else:
                nx = x * dx[d]
                if 0 <= nx <= 100000 and not v[nx]:
                    que.append(nx)
                    v[nx] = v[x] + 1

A, B, N, M = map(int, input().split())

v = [0]*100001
dx = [1, -1, A, B, -A, -B, A, B]

bfs(N)

print(v[M]-1)
