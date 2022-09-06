import sys
sys.stdin = open('7-13 input.txt')


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]

    h = 4
    max_v = 0
    # while True:
    v = [[0]*N for _ in range(N)]
    for x in range(N):
        for y in range(N):
            if data[x][y] > h:
                v[x][y] = 1

    # for d in range(4):
    #     nx = x + dx[d]
    #     ny = y + dy[d]
    #     if 0 <= nx < N and 0 <= ny < N:
    #         if data[nx][ny] > h and data[nx][ny] > data[x][y]:
    #         break
    # else:
    #     v[x][y] = 1


    print(v)




''' [풀이]

'''