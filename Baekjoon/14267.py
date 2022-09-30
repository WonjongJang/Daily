import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def recur(n):
    for d in adj[n]:
        dp[d] += dp[n]
        recur(d)

N, M = map(int, input().split())
data = list(map(int, input().split()))
adj = [[] for _ in range(N+1)]

for i in range(1, N):
    adj[data[i]].append(i+1)

dp = [0]*(N+1)
for _ in range(M):
    i, w = map(int, input().split())
    dp[i] += w

recur(1)

print(*dp[1:])