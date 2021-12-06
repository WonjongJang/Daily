import sys
sys.stdin = open('input.txt')


# 상하좌우 대각선
dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

def bfs(sx, sy):
    q = []
    q.append((sx, sy))
    data[sx][sy] = 2        # visited 대신 지나간 곳을 2로 바꿈

    while q:
        x, y = q.pop(0)

        for d in range(8):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < h and 0 <= ny < w and data[nx][ny] == 1:
                q.append((nx, ny))
                data[nx][ny] = 2

while True:
    w, h = map(int, input().split())    # w : 너비, h : 높이
    data = [list(map(int, input().split())) for _ in range(h)]

    if w == 0 and h == 0:   # 입력 마지막 줄에 0이 주어짐 (입력의 끝)
        break

    cnt = 0     # 섬의 개수
    for f1 in range(h):
        for f2 in range(w):
            if data[f1][f2] == 1:   # 땅이라면
                bfs(f1, f2)         # 진입
                cnt += 1            # 섬 개수 증가

    print(cnt)