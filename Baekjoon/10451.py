import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10**9)


def recur(x, s):
    global cnt
    v[x] = 1

    for a in adj[x]:
        if a == s:
            cnt += 1
            return
        if not v[a]:
            recur(a, s)

T = int(input())
for _ in range(T):
    N = int(input())
    arr1 = list(range(1, N+1))
    arr2 = list(map(int, input().split()))

    adj = [[] for _ in range(N+1)]
    for i in range(N):
        adj[arr1[i]].append(arr2[i])

    v = [0] * (N+1)
    cnt = 0
    for i in range(1, N+1):
        recur(i, i)

    print(cnt)