import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10**5)
input = sys.stdin.readline


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def melt(x, y):
    cnt = 0
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if not data[nx][ny]:
            cnt += 1

    if cnt:
        melt_list.append((x, y, cnt))

def recur(x, y):
    v[x][y] = 1

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 < nx < N-1 and 0 < ny < M-1 and not v[nx][ny] and data[nx][ny]:
            recur(nx, ny)

N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]

year = 0
flag = 0
while True:
    # 빙하 녹이기
    year += 1
    melt_list = []
    for i in range(1, N-1):
        for j in range(1, M-1):
            if data[i][j]:
                melt(i, j)

    for x, y, c in melt_list:
        if data[x][y] - c >= 0:
            data[x][y] -= c
        else:
            data[x][y] = 0

    # 빙하 개수
    island = 0
    v = [[0] * M for _ in range(N)]
    for i in range(1, N-1):
        for j in range(1, M-1):
            if not v[i][j] and data[i][j]:
                island += 1

                if island >= 2:
                    break

                recur(i, j)

    if island >= 2:
        break

    if not sum(map(sum, data[1:-1])):
        year = 0
        break

print(year)



''' [파이썬: 시간 초과, PyPy3: 메모리 초과]
import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10**5)
input = sys.stdin.readline


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def melt(x, y, cnt):
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if not data[nx][ny]:
            cnt += 1

    if data[x][y] - cnt >= 0:
        tot_cnt[x][y] = cnt
    else:
        tot_cnt[x][y] = data[x][y]

def recur(x, y, t):
    v[x][y] = t

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 < nx < N-1 and 0 < ny < M-1 and v[nx][ny] == t-1 and data[nx][ny]:
            recur(nx, ny, t)

N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]

year = 0
v = [[0] * M for _ in range(N)]
flag = 0
while True:
    if not sum(sum(data, [])):
        break

    island = 0

    for i in range(1, N-1):
        for j in range(1, M-1):
            if v[i][j] == year and data[i][j]:
                island += 1
                recur(i, j, year+1)

    if island >= 2:
        flag = 1
        break

    year += 1
    tot_cnt = [[0] * M for _ in range(N)]
    for i in range(1, N-1):
        for j in range(1, M-1):
            if data[i][j]:
                melt(i, j, 0)

    for i in range(1, N-1):
        for j in range(1, M-1):
            data[i][j] -= tot_cnt[i][j]

if flag:
    print(year)
else:
    print(0)
'''