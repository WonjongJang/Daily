import sys
sys.stdin = open('input.txt')


A, B, C = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(3)]

V = [0] * max(x[1] for x in data)

for d in data:
    for i in range(d[0], d[1]):
        V[i] += 1

ans = 0
for v in V:
    if v == 1:
        ans += v*A
    elif v == 2:
        ans += v*B
    else:
        ans += v*C

print(ans)