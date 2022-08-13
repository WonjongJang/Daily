import sys
sys.stdin = open('input.txt')


N, M = map(int, input().split())
data = [int(input()) for _ in range(N)]

s = 0
e = min(data) * M
ans = 0
while s <= e:
    m = (s+e)//2

    cnt = 0
    for d in data:
        cnt += m//d

    if cnt >= M:
        e = m-1
        ans = m
    else:
        s = m+1

print(ans)