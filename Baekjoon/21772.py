import sys
sys.stdin = open('input.txt')


# 상 하 좌 우 (제자리)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def sol(x, y, t, cnt):
    global max_v

    # if max_v == SP:     # 백트래킹 (이미 모든 고구마 다 먹었다면)
    #     return
    if cnt + (T-t) <= max_v:
        return

    if t == T:          # T초 이동 했다면
        max_v = max(max_v, cnt)
        return

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < R and 0 <= ny < C and data[nx][ny] != '#':
            if data[nx][ny] == 'S':         # 이동할 위치에 고구마 있다면
                data[nx][ny] = '.'
                sol(nx, ny, t+1, cnt+1)     # 먹은 고구마 개수(cnt) 1 증가
                data[nx][ny] = 'S'
            else:
                sol(nx, ny, t+1, cnt)

R, C, T = map(int, input().split())         # R: 행, C: 열, T: 이동 시간
data = [list(input()) for _ in range(R)]

SP = 0      # 총 고구마 개수 저장
for r in range(R):
    for c in range(C):
        if data[r][c] == 'S':
            SP += 1
        elif data[r][c] == 'G':   # 가희 현재 위치
            sx = r
            sy = c

max_v = 0   # 최대 먹을 수 있는 고구마 개수

sol(sx, sy, 0, 0)

print(max_v)





# def sol(x, y):
#     global max_v
#
#     q = [(x, y, 0, 0)]
#     visited[x][y] = 1
#
#     while q:
#         x, y, t, cnt = q.pop(0)
#         print(x, y, t, cnt)
#         if t == T:
#             print('왔다')
#             max_v = max(max_v, cnt)
#             continue
#
#         for d in range(4):
#             nx = x + dx[d]
#             ny = y + dy[d]
#             if 0 <= nx < R and 0 <= ny < C and data[nx][ny] != '#' and not visited[nx][ny]:
#                 if data[nx][ny] == 'S':
#                     cnt += 1
#                 visited[nx][ny] = 1
#                 q.append((nx, ny, t+1, cnt))
#
#
# R, C, T = map(int, input().split())     # R: 행, C: 열, T: 이동 시간
# data = [list(input()) for _ in range(R)]
#
# visited = [[0] * C for _ in range(R)]
# print(data)
# print(visited)
#
# for r in range(R):
#     for c in range(C):
#         if data[r][c] == 'G':
#             sx = r
#             sy = c
#
# max_v = 0
#
# sol(sx, sy)

# print(max_v)