import sys
sys.stdin = open('8-11 input.txt')


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    dp = [[float('INF')]*(N+1) for _ in range(N+1)]

    for i in range(1, N+1):
        dp[i][i] = 0

    for _ in range(M):
        f, t, v = map(int, input().split())
        dp[f][t] = v

    for k in range(N+1):
        for i in range(N+1):
            for j in range(N+1):
                dp[i][j] = min(dp[i][j], dp[i][k]+dp[k][j])

    for i in range(1, N+1):
        for j in range(1, N+1):
            if dp[i][j] == float('INF'):
                print('M', end=' ')
            else:
                print(dp[i][j], end=' ')
        print()



''' [풀이]

'''