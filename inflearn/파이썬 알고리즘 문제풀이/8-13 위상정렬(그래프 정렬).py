import sys
sys.stdin = open('8-13 input.txt')


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    adj = [[0]*(N+1) for _ in range(N+1)]
    degree = [0]*(N+1)
    ans = []

    for _ in range(M):
        b, a = map(int, input().split())
        adj[b][a] = 1
        degree[a] += 1

    for i in range(1, N+1):
        if degree[i] == 0:
            ans.append(i)

    while ans:
        x = ans.pop(0)
        print(x, end=' ')
        for i in range(1, N+1):
            if adj[x][i] == 1:
                degree[i] -= 1
                if degree[i] == 0:
                    ans.append(i)



''' [풀이]
import sys
from collections import deque
sys.stdin=open("input.txt", "r")
n, m=map(int, input().split())
graph=[[0]*(n+1) for _ in range(n+1)]
degree=[0]*(n+1)
dQ=deque()
for i in range(m):
    a, b=map(int, input().split())
    graph[a][b]=1
    degree[b]+=1
for i in range(1, n+1):
    if degree[i]==0:
        dQ.append(i)
while dQ:
    x=dQ.popleft()
    print(x, end=' ')
    for i in range(1, n+1):
        if graph[x][i]==1:
            degree[i]-=1
            if degree[i]==0:
                dQ.append(i)
'''