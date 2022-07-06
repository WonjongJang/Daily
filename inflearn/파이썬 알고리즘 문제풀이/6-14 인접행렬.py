import sys
sys.stdin = open('6-14 input.txt', 'rt')


# 전체 반복 횟수
T = int(input())

# 전체 반복
for tc in range(1, T+1):
    N, M = map(int, input().split())

    adj = [[0] * N for _ in range(N)]

    for i in range(M):
        s, e, w = map(int, input().split())
        adj[s-1][e-1] = w

    print(adj)



''' [풀이]
n=int(input())
m=int(input())
g=[[0]*(n+1) for _ in range(n+1)]
for i in range(m):
    a, b=map(int, input().split())
    g[a][b]=1
    g[b][a]=1

for i in range(1, n+1):
    for j in range(1, n+1):
        print(g[i][j], end=' ')
    print()
'''