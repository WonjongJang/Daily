import sys
sys.stdin = open('input.txt')


move = {
    'R': (0, 1),
    'L': (0, -1),
    'B': (-1, 0),
    'T': (1, 0),
    'RT': (1, 1),
    'LT': (1, -1),
    'RB': (-1, 1),
    'LB': (-1, -1)
}

trans = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7
}

K, S, N = map(str, input().split())


kx = int(K[1])-1
ky = trans[K[0]]

print(kx, ky)
sx = int(S[1])-1
sy = trans[S[0]]

N = int(N)
for _ in range(N):
    m = input()
    mx, my = move[m][0], move[m][1]

    nkx, nky = kx+mx, ky+my
    print(nkx, nky)
    if 0 <= nkx < 8 and 0 <= nky < 8:   # 킹이 체스판 밖으로 나가지 않는 경우
        if nkx == sx and nky == sy:     # 움직이려는 곳에 돌이 있다면
            nsx, nsy = sx+mx, sy+my
            if 0 <= nsx < 8 and 0 <= nsy < 8:   # 돌이 밀려날 때 체스판 밖으로 나가지 않는 경우

        else:   # 움직이려는 곳에 돌이 없다면
            kx, ky = nkx, nky

print(kx, ky)