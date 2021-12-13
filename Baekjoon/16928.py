import sys
sys.stdin = open('input.txt')
from collections import deque


def check_ladder(x):                # 사다리 체크
    for i in range(len(ladder)):
        if x == ladder[i][0]:
            return ladder[i][1]
    return 0

def check_snake(x):                 # 뱀 체크
    for i in range(len(snake)):
        if x == snake[i][0]:
            return snake[i][1]
    return 0

def sol(s, e):
    global min_cnt

    q = deque()
    q.append((s, 0))    # 시작 위치 저장
    visited[s] = 1      # 방문

    while q:
        t, c = q.popleft()

        if t == e:      # 도착
            min_cnt = min(min_cnt, c)

        for d in range(1, 7):       # 주사위 굴려서 갈 수 있는 모든 거리
            nt = t + d
            nc = c + 1
            up = check_ladder(nt)   # 사다리 있을 때 이동할 위치 저장
            down = check_snake(nt)  # 뱀 있을 때 이동할 위치 저장

            if nt <= 100 and visited[nt] == 0:  # 100 이하, 방문하지 않았으면
                visited[nt] = 1                 # 방문
                if up:                          # 방문한 곳이 사다리일 때
                    q.append((up, nc))
                elif down:                      # 방문한 곳이 뱀일 때
                    q.append((down, nc))
                else:
                    q.append((nt, nc))

N, M = map(int, input().split())    # N: 사다리 수, M: 뱀 수
ladder = [list(map(int, input().split())) for _ in range(N)]
snake = [list(map(int, input().split())) for _ in range(M)]

start = 1
end = 100

visited = [0] * 101     # 방문 표시
min_cnt = 100000        # 주사위 굴린 횟수 최소값

sol(start, end)

print(min_cnt)