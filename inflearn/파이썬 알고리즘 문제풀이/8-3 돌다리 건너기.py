import sys
sys.stdin = open('8-3 input.txt')


T = int(input())
for tc in range(1, T+1):
    N = int(input())

    dp = [0] * (N+2)

    dp[1] = 1
    dp[2] = 2
    for i in range(3, N+2):
        dp[i] = dp[i-1] + dp[i-2]

    print(dp[N+1])



''' [풀이]
import sys
sys.stdin = open("input.txt", 'r')
n=int(input())
dy=[0]*(n+1)
dy[1]=1
dy[2]=2
for i in range(3, n+2):
    dy[i]=dy[i-1]+dy[i-2]

print(dy[n+1])
'''