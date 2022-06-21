import sys
sys.stdin = open('1-4 input.txt', 'rt')


# 전체 반복 횟수
T = int(input())

# 전체 반복
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    mean = int(sum(arr) / N + 0.5)  # round half up (round 함수는 round half even)

    tmp = list(map(lambda x: x-mean, arr))

    min_v = (0, tmp[0], abs(tmp[0]))
    for i in range(1, N):
        if min_v[2] > abs(tmp[i]):
            min_v = (i, tmp[i],abs(tmp[i]))
        elif min_v[2] == abs(tmp[i]):
            if min_v[1] < tmp[i]:
                min_v = (i, tmp[i], abs(tmp[i]))

    print(mean, min_v[0] + 1)