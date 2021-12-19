import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10**4)


# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def sol(x, y):
    global cnt

    space[x][y] = 2     # 방문한 곳을 2로 바꾸면 visited 만들지 않아도 됨
    cnt += 1

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < N and 0 <= ny < M and space[nx][ny] == 1:
            sol(nx, ny)

N, M, K = map(int, input().split())     # N: 가로, M: 세로, K: 음식물 쓰레기 개수

space = [[0] * M for _ in range(N)]     # 통로

for k in range(K):
    x, y = map(int, input().split())
    space[x-1][y-1] = 1                 # 쓰레기 위치 입력

max_v = 0   # 가장 큰 음식물 크기

for n in range(N):
    for m in range(M):
        if space[n][m] == 1:        # 쓰레기 있다면
            cnt = 0
            sol(n, m)
            max_v = max(max_v, cnt)

# 출력
print(max_v)



# [bfs]
import sys
sys.stdin = open('input.txt')


# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def sol(sx, sy):
    global cnt

    space[sx][sy] = 2     # 방문한 곳을 2로 바꾸면 visited 만들지 않아도 됨
    cnt += 1

    q = [(sx, sy)]
    while q:
        x, y = q.pop(0)
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < M and space[nx][ny] == 1:
                space[nx][ny] = 2
                cnt += 1
                q.append((nx, ny))

N, M, K = map(int, input().split())     # N: 가로, M: 세로, K: 음식물 쓰레기 개수

space = [[0] * M for _ in range(N)]     # 통로

for k in range(K):
    x, y = map(int, input().split())
    space[x-1][y-1] = 1                 # 쓰레기 위치 입력

max_v = 0   # 가장 큰 음식물 크기

for n in range(N):
    for m in range(M):
        if space[n][m] == 1:        # 쓰레기 있다면
            cnt = 0
            sol(n, m)
            max_v = max(max_v, cnt)

# 출력
print(max_v)