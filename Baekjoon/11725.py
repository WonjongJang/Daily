import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10**9)


def recur(x):
    for i in adj[x]:
        if par[i] == 0:
            par[i] = x
            recur(i)

N = int(input())

adj = [[] for _ in range(N+1)]
par = [0] * (N+1)

for _ in range(N-1):
    n1, n2 = map(int, input().split())

    adj[n1].append(n2)
    adj[n2].append(n1)

par[1] = -1
recur(1)

for i in range(2, N+1):
    print(par[i])