import sys
sys.stdin = open('input.txt')


def recur(L, sum_p):
    global max_v
    sum_p += P[L]
    print(L)

    for i in range(adj[L], N+1):
        if i <= N and adj[i] <= N+1:
            recur(i, sum_p)

    print(sum_p)
    max_v = max(max_v, sum_p)

N = int(input())
adj = [0]*(N+1)
P = [0]*(N+1)
for i in range(1, N+1):
    t, p = map(int, input().split())

    adj[i] = i+t
    P[i] = p

print(adj)
print(P)
max_v = 0
for s in range(1, N+1):
    if adj[s] <= N+1:
        recur(s, 0)

print(max_v)



''' dp 풀이
n = int(input())
t = []
p = []
dp = []
for i in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)
    dp.append(b)
dp.append(0)
print(dp)
for i in range(n - 1, -1, -1):
    if t[i] + i > n:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(dp[i + 1], p[i] + dp[i + t[i]])
print(dp)
'''