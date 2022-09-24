import sys
sys.stdin = open('input.txt')


N = int(input())

if N > 2:
    dp = [0] * (N+1)
    dp[1] = 1
    dp[2] = 1
    for i in range(3, N+1):
        dp[i] = dp[i-1] + dp[i-2]

    print(dp[N])
else:
    print(1)