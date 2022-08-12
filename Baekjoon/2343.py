import sys
sys.stdin = open('input.txt')


N, M = map(int, input().split())
data = list(map(int, input().split()))

s = max(data)
e = sum(data)
ans = 2147000000
while s <= e:
    blue = [0] * M

    m = (s+e)//2
    idx = 0
    for i in range(N):
        if blue[idx]+data[i] <= m:
            blue[idx] += data[i]
        else:
            idx += 1
            if idx >= M:
                break
            else:
                blue[idx] += data[i]

    if idx >= M:
        s = m+1
    else:
        e = m-1
        ans = min(ans, m)

print(ans)