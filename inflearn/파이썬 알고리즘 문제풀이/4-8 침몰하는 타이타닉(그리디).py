import sys
sys.stdin = open('4-8 input.txt', 'rt')


# 전체 반복 횟수
T = int(input())

# 전체 반복
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    arr.sort(reverse=True)

    cnt = 0
    while arr:
        if len(arr) == 1:
            cnt += 1
            break
        if arr[0] + arr[-1] <= M:
            arr.pop(0)
            arr.pop(-1)
            cnt += 1
        else:
            arr.pop(0)
            cnt += 1

    print(cnt)



''' [풀이]
from collections import deque

n, limit=map(int, input().split())
p=list(map(int, input().split()))
p.sort()
p=deque(p)
cnt=0
while p:
    if len(p)==1:
        cnt+=1
        break
    if p[0]+p[-1]>limit:
        p.pop()
        cnt+=1
    else:
        p.popleft()
        p.pop()
        cnt+=1
print(cnt)
'''