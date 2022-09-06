import sys
sys.stdin = open('input.txt')


T = 0
while True:
    T += 1
    N = int(input())
    if N == 0:
        break

    adj = {}
    v = {}
    for n in range(N):
        f, t = map(str, input().split())
        adj[f] = t
        v[f] = 0

    cnt = 0
    for s in adj:
        if v[s] == 0:
            tmp = s
            while True:
                v[tmp] = 1

                if v[adj[tmp]] == 0:
                    tmp = adj[tmp]
                elif v[adj[tmp]] and adj[tmp] == s:
                    cnt += 1
                    break
                else:
                    break

    print(T, cnt)