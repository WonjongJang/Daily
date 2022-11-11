import sys
sys.stdin = open('input.txt')
from collections import deque


N, K = map(int, input().split())
que = deque(x for x in range(1, N+1))

ans = deque()
cnt = 0
while que:
    x = que.popleft()
    cnt += 1

    if cnt == K:
        cnt = 0
        ans.append(x)
    else:
        que.append(x)

print('<' + ', '.join(map(str, ans)) + '>')