import sys
sys.stdin = open('input.txt')


N = int(input())
data = list(map(int, input().split()))

dp = [0]*N
dp[0] = 1
for i in range(1, N):
    max_v = 0
    for j in range(i-1, -1, -1):
        if data[i] > data[j]:
            max_v = max(max_v, dp[j])

    dp[i] = max_v+1

print(max(dp))