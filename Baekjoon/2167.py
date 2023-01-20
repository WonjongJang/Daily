import sys
sys.stdin = open('input.txt')


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
K = int(input())
K_list = [list(map(int, input().split())) for _ in range(K)]
dp = [[0]*(M+1) for _ in range(N+1)]

for n in range(1, N+1):
    for m in range(1, M+1):
        dp[n][m] = arr[n-1][m-1] + dp[n][m-1] + dp[n-1][m] - dp[n-1][m-1]   # 기존 arr 위치값 + 왼쪽 누적합 + 위쪽 누적합 - 교집합

for k in range(K):
   i, j, x, y = K_list[k]
   print(dp[x][y] - dp[x][j-1] - dp[i-1][y] + dp[i-1][j-1])



# 시간 초과
# N, M = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]
# K = int(input())
# K_list = [list(map(int, input().split())) for _ in range(K)]
#
# res = [0]*K # K개의 합을 구하기 때문에 개수 만큼 초기화
# for k in range(K):
#     i, j, x, y = K_list[k]
#     for n in range(i-1, x): # i-1 부터 x-1 까지
#         for m in range(j-1, y): # j-1 부터 y-1 까지
#             res[k] += arr[n][m] # 수들의 합
#
# for r in res:
#     print(r)