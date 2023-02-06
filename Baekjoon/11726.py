import sys
sys.stdin = open('input.txt')


n = int(input())
if n > 2:
    dp = [0]*(n+1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = (dp[i-1] + dp[i-2]) % 10007
    print(dp[n])
else:
    print(n)



# N = int(input())
#
# if N > 2:
#     dp = [0] * (N+1)
#
#     dp[1] = 1
#     dp[2] = 2
#     for i in range(3, N+1):
#         dp[i] = dp[i-1] + dp[i-2]
#
#     print(dp[N] % 10007)
# else:
#     print(N)