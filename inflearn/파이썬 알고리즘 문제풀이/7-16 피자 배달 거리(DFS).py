import sys
sys.stdin = open('7-16 input.txt')


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def recur(L, s):
    if L == M:
        global ans

        sum = 0
        for hx, hy in hs:
            d = 2147000000
            for r in res:
                rx, ry = r[0], r[1]
                d = min(d, abs(hx-rx)+abs(hy-ry))
            sum += d
        ans = min(ans, sum)
    else:
        for i in range(s, len(pz)):
            res.append(pz[i])
            recur(L+1, i+1)
            res.pop()


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]

    hs = []
    pz = []
    for x in range(N):
        for y in range(N):
            if data[x][y] == 1:
                hs.append((x, y))
            if data[x][y] == 2:
                pz.append((x, y))

    res = []
    ans = 2147000000
    recur(0, 0)
    print(ans)






''' [풀이]

'''