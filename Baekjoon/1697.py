import sys
sys.stdin = open('input.txt')
from collections import deque


dx = [-1, 1, 2]

N, K = map(int, input().split())

v = [0] * 100001
que = deque()
que.append((N, 0))
v[N] = 1

while que:
    x, c = que.popleft()

    if x == K:
        print(c)
        break

    for d in range(3):
        if d == 2:
            nx = x * dx[d]
        else:
            nx = x + dx[d]
        if 0 <= nx <= 100000 and not v[nx]:
            que.append((nx, c+1))
            v[nx] = 1
