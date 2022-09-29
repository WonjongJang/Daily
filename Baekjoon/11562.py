import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
INF = float('inf')

N, M = map(int, input().split())
graph = [[INF]*(N+1) for _ in range(N+1)]

for i in range(1, N+1): # 자기 자신
    graph[i][i] = 0

for _ in range(M):
    u, v, b = map(int, input().split())
    if b:
        graph[u][v] = 0
        graph[v][u] = 0
    else:
        graph[u][v] = 0
        graph[v][u] = 1

for k in range(1, N+1):
    for a in range(1, N+1):
        for b in range(1, N+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

K = int(input())
for _ in range(K):
    s, e = map(int, input().split())
    print(graph[s][e])



''' [시간 초과]
from collections import deque

N, M = map(int, input().split())
adj = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    u, v, b = map(int, input().split())
    if b:
        adj[u][v] = 2
        adj[v][u] = 2
    else:
        adj[u][v] = 2
        adj[v][u] = 1

K = int(input())
for _ in range(K):
    s, e = map(int, input().split())

    cnt = 0
    if s == e:
        print(cnt)
        continue

    v = [0]*(N+1)
    que = deque()
    que.append((s, 0))
    v[s] = 1

    while que:
        x, cnt = que.popleft()

        if x == e:
            print(cnt)
            break

        for d in range(N+1):
            if not v[d]:
                if adj[x][d] == 2:
                    que.append((d, cnt))
                    v[d] = 1
                elif adj[x][d] == 1:
                    que.append((d, cnt+1))
                    v[d] = 1
'''