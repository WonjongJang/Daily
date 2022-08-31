import sys
sys.stdin = open('input.txt')

import heapq


# 하우상좌
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

TC = 0          # 테스트 케이스
while True:
    TC += 1     # 테스트 케이스 마다 1씩 증가

    N = int(input())    # N: 동굴의 크기

    if not N:   # 테스트 케이스 끝
        break

    cave = [list(map(int, input().split())) for _ in range(N)]

    dist = [[99999999 for _ in range(N)] for _ in range(N)]

    que = []
    heapq.heappush(que, [cave[0][0], 0, 0])         # 시작점부터 도둑 루피 존재할 수 있기 때문에 0이 아닌 cave[0][0]로 처리
    dist[0][0] = cave[0][0]

    while que:
        s, x, y = heapq.heappop(que)

        if x == N-1 and y == N-1:                   # 도착
            print('Problem {}: {}'.format(TC, s))
            break

        if dist[x][y] < s:                          # 백트래킹
            continue

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < N:
                ns = s + cave[nx][ny]
                if dist[nx][ny] > ns:
                    dist[nx][ny] = ns
                    heapq.heappush(que, [ns, nx, ny])



'''
import sys
sys.stdin = open('input.txt')
INF = sys.maxsize


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

T = 1
while True:
    N = int(input())
    if N == 0:
        break
    data = [list(map(int, input().split())) for _ in range(N)]

    dist = [[INF]*(N) for _ in range(N)]

    q = []
    q.append((0, 0))
    dist[0][0] = data[0][0]

    while q:
        x, y = q.pop(0)

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < N:
                if dist[x][y] + data[nx][ny] < dist[nx][ny]:
                    dist[nx][ny] = dist[x][y] + data[nx][ny]
                    q.append((nx, ny))

    print('Problem {}: {}'.format(T, dist[N-1][N-1]))
    T += 1
'''