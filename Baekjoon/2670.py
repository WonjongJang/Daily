import sys
sys.stdin = open('input.txt')


N = int(input())
data = [float(input()) for _ in range(N)]

dp = [0]*N
dp[0] = data[0]
dp[1] = max(data[1], data[0]*data[1])
for i in range(2, N):
    dp[i] = max(data[i], data[i]*dp[i-1])

print('{:.3f}'.format(max(dp)))