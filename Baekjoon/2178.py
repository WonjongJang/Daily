import sys
sys.stdin = open('input.txt')


# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(sx, sy):
    q = []                  # 큐 생성
    q.append((sx, sy))      # 시작점 추가
    visited[sx][sy] = 1     # 방문 표시

    while q:
        x, y = q.pop(0)     # 큐 앞에서 부터 빼옴

        if x == N-1 and y == M-1:   # 도착 위치이면
            return x, y             # 위치와 함께 리턴

        for d in range(4):  # 네 방향으로 갈 수 있는 곳 탐색
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < M and data[nx][ny] == '1' and visited[nx][ny] == 0:    # 조건 맞으면
                q.append((nx, ny))                      # 큐에 추가
                visited[nx][ny] = visited[x][y] + 1     # 이전 위치에서의 visited 값에 1을 더하며 이동

N, M = map(int, input().split())    # N x M
data = [list(input()) for _ in range(N)]

visited = [[0] * M for _ in range(N)]   # 방문 표시하며 cnt

x, y = bfs(0, 0)    # 최단거리는 bfs

print(visited[x][y])