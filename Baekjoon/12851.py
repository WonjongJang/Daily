import sys
sys.stdin = open('input.txt')
from collections import deque


N, K = map(int, input().split())

v = [-1] * 100001
que = deque()
que.append(N)
v[N] = 0

cnt = 0
while que:
    x = que.popleft()

    if x == K:
        cnt += 1

    for nx in [x-1, x+1, x*2]:
        if 0 <= nx < 100001:
            if v[nx] == -1 or v[nx] >= v[x]+1:
                v[nx] = v[x] + 1
                que.append(nx)

print(v[K])
print(cnt)