import sys
sys.stdin = open('input.txt')


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def recur(x, y):
    global cnt

    arr[x][y] = 2
    cnt += 1

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 1:
            recur(nx, ny)

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]

cnt_list = []
tot_cnt = 0
for i in range(N):
    for j in range(N):
        cnt = 0
        if arr[i][j] == 1:
            tot_cnt += 1
            recur(i, j)
            cnt_list.append(cnt)

cnt_list.sort()

print(tot_cnt)
print('\n'.join(map(str, cnt_list)))