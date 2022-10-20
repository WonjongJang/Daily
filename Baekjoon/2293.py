import sys
sys.stdin = open('input.txt')


N, K = map(int, input().split())
dp = [0]*(K+1)
dp[0] = 1
for _ in range(N):
    c = int(input())
    for i in range(c, K+1):
        if i-c >= 0:
            dp[i] += dp[i-c]

print(dp[K])