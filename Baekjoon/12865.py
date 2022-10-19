import sys
sys.stdin = open('input.txt')


N, K = map(int, input().split())
dp = [0]*(K+1)
for _ in range(N):
    w, k = map(int, input().split())
    print(w, k)
    for i in range(w, K+1, 1):
        dp[i] = max(dp[i], k, )

print(dp)