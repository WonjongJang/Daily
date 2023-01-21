import sys
sys.stdin = open('input.txt')


N = int(input())
dp = [[0]*10 for _ in range(N+1)]

# 마지막 자리가 0~9로 끝나는 것의 개수로 규칙 찾음 (좌우 대각선 위의 값을 합친 것)
for i in range(1, 10):  # N=1, 즉 한자리 수일 때 1에서 9까지 1개씩 초기화 (0으로 시작할 수 없기 때문에 한자리 수는 0 제외)
    dp[1][i] = 1

for i in range(2, N+1): # 두자리 수 부터 N자리 수 까지
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][j+1] # 오른쪽 위 대각선 밖에 없음
        elif j == 9:
            dp[i][j] = dp[i-1][j-1] # 왼쪽 위 대각선 밖에 없음
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]  # 좌우 대각선 위

print(sum(dp[N]) % 1000000000)



# 시간 초과
# def recur(s, idx):
#     global ans
#
#     if idx == N-1:
#         # print(number)
#         ans += 1
#         return
#
#     ms = s-1
#     ps = s+1
#     n_idx = idx+1
#     if 0 <= ms <= 9:
#         number[n_idx] = ms
#         recur(ms, n_idx)
#         number[n_idx] = 0
#     if 0 <= ps <= 9:
#         number[n_idx] = ps
#         recur(ps, n_idx)
#         number[n_idx] = 0
#
# N = int(input())
# number = [0]*N
#
# ans = 0
# for start in range(1, 10):
#     number[0] = start
#     recur(start, 0)
#     number[0] = 0
#
# print(ans % 1000000000)