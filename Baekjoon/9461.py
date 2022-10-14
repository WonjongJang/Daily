import sys
sys.stdin = open('input.txt')


T = int(input())
for _ in range(T):
    N = int(input())

    if N > 3:
        dp = [0]*(N+1)
        dp[1] = 1
        dp[2] = 1
        dp[3] = 1
        for i in range(4, N+1):
            dp[i] = dp[i-2] + dp[i-3]
        print(dp[N])
    else:
        print(1)



# T = int(input())
#
# for tc in range(1, T+1):
#     N = int(input())
#
#     P = [0, 1, 1, 1]
#
#     if N == 1 or N == 2 or N == 3:
#         ans = P[N]
#     else:
#         n = 4
#         while True:
#             if n > N:
#                 break
#
#             P_new = P[n-3] + P[n-2]
#             P.append(P_new)
#
#             n += 1
#         ans= P[N]
#
#     print(ans)