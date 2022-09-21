import sys
sys.stdin = open('input.txt')


T = int(input())
for _ in range(T):
    N = int(input())

    if N > 3:
        dp = [0] * (N+1)
    else:
        dp = [0] * 4

    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    for i in range(4, N+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

    print(dp[N])