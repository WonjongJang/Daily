import sys
sys.stdin = open('input.txt')


# 전체 반복 횟수
T = int(input())

# 전체 반복
for tc in range(1, T+1):
    N = int(input())    # N*N
    data = [list(map(int, input().split())) for _ in range(N)]

    print(data)

    stairs = []
    for i in range(N):
        for j in range(N):
            if data[i][j] != 0 and data[i][j] != 1:
                stairs.append((i, j))

    print(stairs)
    dist = []
    for i in range(N):
        for j in range(N):
            if data[i][j] == 1:
                dist.append(abs(i-stairs[0][0]) + abs(j-stairs[0][1]))

    print(dist)