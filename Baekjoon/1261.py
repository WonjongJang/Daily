import sys
sys.stdin = open('input.txt')

import heapq


# 하우상좌
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

M, N = map(int, input().split())    # M: 가로, N: 세로
maze = [list(input()) for _ in range(N)]

dist = [[99999999 for _ in range(M)] for _ in range(N)]

que = []
heapq.heappush(que, [0, 0, 0])      # 항상 [0, 0, 0]에서 첫번째 요소가 합계 (heapq 동작 위해)
dist[0][0] = 0

while que:
    s, x, y = heapq.heappop(que)

    if x == N-1 and y == M-1:       # 도착
        print(s)
        break

    if dist[x][y] < s:              # 백트래킹
        continue

    for d in range(4):      # 네 방향으로 이동
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < N and 0 <= ny < M:     # 미로 안이라면
            ns = s + int(maze[nx][ny])      # s에 부순 벽을 더함 (벽이 없다면 0이 더해짐)
            if dist[nx][ny] > ns:           # 항상 그 위치로 갈 수 있는 최소값이라면 저장
                dist[nx][ny] = ns
                heapq.heappush(que, [ns, nx, ny])