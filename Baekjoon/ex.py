import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10**6)


dx = [-1, 0, 1, 0, -1, -1, 1, 1]
dy = [0, 1, 0, -1, -1, 1, -1, 1]

def recur(x, y):
    arr[x][y] = 2

    for d in range(8):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < h and 0 <= ny < w and arr[nx][ny] == 1:
            recur(nx, ny)

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    arr = [list(map(int, input().split())) for _ in range(h)]

    cnt = 0
    for x in range(h):
        for y in range(w):
            if arr[x][y] == 1:
                cnt += 1
                recur(x, y)

    print(cnt)