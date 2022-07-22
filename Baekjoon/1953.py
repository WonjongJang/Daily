import sys
sys.stdin = open('input.txt')


def recur(x, team):
    v[x] = team

    for i in adj[x]:
        if not v[i]:
            recur(i, -team)

N = int(input())
adj = [[] for _ in range(N+1)]
v = [0] * (N+1)
for n in range(N):
    tmp = list(map(int, input().split()))
    for t in tmp[1:]:
        adj[n+1].append(t)

for i in range(1, N+1):
    if not v[i]:
        if i%2:
            recur(i, 1)
        else:
            recur(i, -1)

B = []
W = []
for i in range(N+1):
    if v[i] == 1:
        B.append(i)
    elif v[i] == -1:
        W.append(i)

print(len(B))
print(*B)
print(len(W))
print(*W)