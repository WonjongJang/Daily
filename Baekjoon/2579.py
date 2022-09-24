import sys
sys.stdin = open('input.txt')


N = int(input())
data = [0]+[int(input()) for _ in range(N)]

if N >= 3:
    dp = [0] * (N+1)
    dp[1] = data[1]
    dp[2] = data[1]+data[2]
    dp[3] = max(data[1]+data[3], data[2]+data[3])
    for i in range(4, N+1):
        dp[i] = max(dp[i-3]+data[i-1], dp[i-2]) + data[i]

    print(dp[N])
else:
    print(sum(data))