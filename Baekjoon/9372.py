import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def recur(n):
    global cnt
    v[n] = 1

    for i in ch[n]:
        if not v[i]:
            recur(i)
            cnt += 1

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    v = [0]*(N+1)
    ch = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        ch[a].append(b)
        ch[b].append(a)

    cnt = 0
    recur(1)

    print(cnt)