import sys
sys.stdin = open('input.txt')


N = int(input())
data = [int(input()) for _ in range(N)]

dp = [0]*N
dp[0] = 1
for i in range(1, N):
    a = []
    for j in range(i):
        if data[i] > data[j]:
            a.append(dp[j])
    if not a:
        dp[i] = 1
    else:
        dp[i] = max(a) + 1

print(N-max(dp))