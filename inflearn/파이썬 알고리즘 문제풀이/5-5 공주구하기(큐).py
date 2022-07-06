import sys
sys.stdin = open('5-5 input.txt', 'rt')


# 전체 반복 횟수
T = int(input())

# 전체 반복
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(range(1, N+1))

    cnt = 0
    while len(arr) > 1:
        cnt += 1

        if cnt%K:
            tmp = arr.pop(0)
            arr.append(tmp)
        else:
            arr.pop(0)

    print(*arr)


''' [풀이]
from collections import deque

n, k=map(int, input().split())
q=list(range(1, n+1))
dq=deque(q)
while dq:
    for _ in range(k-1):
        cur=dq.popleft()
        dq.append(cur)
    dq.popleft()
    if len(dq)==1:
        print(dq[0])
        dq.popleft()
'''