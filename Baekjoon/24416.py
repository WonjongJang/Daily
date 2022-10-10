import sys
sys.stdin = open('input.txt')


def fibonacci(x):
    global cnt
    dp[1] = 1
    dp[2] = 1
    for i in range(3, n+1):
        dp[i] = dp[i-1]+dp[i-2]
        cnt += 1
    return dp[x]

n = int(input())

dp = [0]*(n+1)
cnt = 0

print(fibonacci(n), cnt)