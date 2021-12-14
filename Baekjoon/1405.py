import sys
sys.stdin = open('input.txt')


# 동서남북 (우좌하상)
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def sol(x, y, cnt, N, p):
    global sum
    # print(x, y, cnt, p)
    if cnt == N:
        # print('도착', x, y)
        sum += p
        return

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if plane[nx][ny] == 0:
            plane[nx][ny] = 1
            sol(nx, ny, cnt+1, N, p*data[d])
            plane[nx][ny] = 0

data = list(map(int, input().split()))
N = data.pop(0)
for _ in range(4):
    data[_] /= 100

plane = [[0] * 29 for _ in range(29)]
sum = 0

# print(N, data)

plane[14][14] = 1
sol(14, 14, 0, N, 1)

print(sum)