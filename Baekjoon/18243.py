import sys
sys.stdin = open('input.txt')


def bfs(s):
    v = [0] * (N + 1)
    que = []
    que.append((s, 0))
    v[s] = 1

    while que:
        n, cnt = que.pop(0)

        if cnt > 6:
            return 0

        for i in adj[n]:
            if not v[i]:
                que.append((i, cnt+1))
                v[i] = 1

    if sum(v) == N:
        return 1
    else:
        return 0

N, K = map(int, input().split())
adj = [[] for _ in range(N+1)]
for _ in range(K):
    A, B = map(int, input().split())
    adj[A].append(B)
    adj[B].append(A)

check = 1
for s in range(1, N+1):
    if not bfs(s):
        check = 0
        break

if check:
    print("Small World!")
else:
    print("Big World!")