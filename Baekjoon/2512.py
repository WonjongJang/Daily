import sys
sys.stdin = open('input.txt')


N = int(input())
req = list(map(int, input().split()))
tot = int(input())

s, e = 0, max(req)     # 상한액

while s<=e:
    m = (s+e) // 2
    sum = 0
    for r in req:
        if r <= m:
            sum += r
        else:
            sum += m

    if sum <= tot:
        s = m+1
    else:
        e = m-1

print(e)



''' [시간초과]
N = int(input())
req = list(map(int, input().split()))
tot = int(input())

supr = max(req)     # 상한액

while True:
    sum = 0
    for r in req:
        if r <= supr:
            sum += r
        else:
            sum += supr

    if sum <= tot:
        break
    else:
        supr -= 1

print(supr)
'''