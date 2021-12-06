import sys
sys.stdin = open('input.txt')

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    global virus_cnt
    queue = []
    visited = [[0] * M for _ in range(N)]

    for v in range(len(V)):
        queue.append(V[v])
        visited[V[v][0]][V[v][1]] = 1

    while queue:
        x, y = queue.pop(0)

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < M and data[nx][ny] == 0 and visited[nx][ny] == 0:
                queue.append([nx, ny])
                visited[nx][ny] = 1

    cnt = 0
    for v1 in range(N):
        for v2 in range(M):
            if visited[v1][v2] == 1:
                cnt += 1
    # print(cnt)
    virus_cnt = min(virus_cnt, cnt)

def build(wall):
    for w in range(3):
        data[wall[w][0]][wall[w][1]] = 1

    bfs()

    for w in range(3):
        data[wall[w][0]][wall[w][1]] = 0

def nCr(n, r, k):   # n개 중 r개를 뽑음. k는 카운트
    if r == k:
        # print(wall)
        build(wall)
    else:
        for i in range(n):          # B 순회
            if used[i] == 0:        # B의 i번째 인자가 사용되지 않았다면
                used[i] = 1         # 사용 표시 후
                wall[k] = B[i]      # wall에 저장
                nCr(n, r, k+1)      # k를 1 증가하며 재귀
                used[i] = 0         # 사용 후 제자리

N, M = map(int, input().split())    # N : 세로, M : 가로
data = [list(map(int, input().split())) for _ in range(N)]

B = []  # 0 영역
V = []  # 2 영역

wall_cnt = 0        # 벽 개수
virus_cnt = 100000  # 바이러스 개수 (min 작업을 위해 큰 값으로 초기화)

for f1 in range(N):
    for f2 in range(M):
        if data[f1][f2] == 2:   # 2 이면
            V.append([f1, f2])  # V에 추가
        elif data[f1][f2] == 0: # 0 이면
            B.append([f1, f2])  # B에 추가
        else:                   # 1 이면
            wall_cnt += 1       # 벽 개수 세기

# 순열
len_B = len(B)
wall = [0] * 3          # 3개의 벽을 담을 곳
used = [0] * len_B      # B 중에 사용한 것 표시
nCr(len_B, 3, 0)

ans = (N*M) - ((wall_cnt+3) + virus_cnt)

print(ans)