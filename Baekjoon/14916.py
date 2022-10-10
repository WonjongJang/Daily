import sys
sys.stdin = open('input.txt')
INF = float('inf')


n = int(input())

coins = [2, 5]
dp = [INF]*(n+1)

dp[0] = 0
for i in range(2):
    for j in range(coins[i], n+1):
        dp[j] = min(dp[j], dp[j-coins[i]]+1)

if dp[n] == INF:
    print(-1)
else:
    print(dp[n])