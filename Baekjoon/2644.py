import sys
sys.stdin = open('input.txt')


def recur(x, cnt):
    global ans
    if x == n2:
        ans = cnt
        return

    for i in adj[x]:
        if not v[x]:
            v[x] = 1
            recur(i, cnt+1)
            v[x] = 0


N = int(input())
n1, n2 = map(int, input().split())
M = int(input())

adj = [[] for _ in range(N+1)]
v = [0] * (N+1)

for _ in range(M):
    p, c = map(int, input().split())

    adj[p].append(c)
    adj[c].append(p)

ans = -1
recur(n1, 0)

print(ans)