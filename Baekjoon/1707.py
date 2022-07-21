import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def recur(x, g):
    v[x] = g

    for i in adj[x]:
        if not v[i]:
            if not recur(i, -g):
                return 0
        elif v[x] == v[i]:
            return 0
    return 1

T = int(input())
for _ in range(T):
    V, E = map(int, input().split())
    adj = [[] for _ in range(V + 1)]
    v = [0] * (V + 1)
    for _ in range(E):
        v1, v2 = map(int, input().split())
        adj[v1].append(v2)
        adj[v2].append(v1)

    ans = 1
    for i in range(1, V+1):
        if not v[i]:
            ans = recur(i, 1)
            if not ans:
                break

    print("YES" if ans else "NO")