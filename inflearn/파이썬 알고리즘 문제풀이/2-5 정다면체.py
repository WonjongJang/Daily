import sys
sys.stdin = open('1-5 input.txt', 'rt')


# 전체 반복 횟수
T = int(input())

# 전체 반복
for tc in range(1, T+1):
    N, M = map(int, input().split())

    arr_N = list(range(1, N+1))
    arr_M = list(range(1, M+1))

    cnt = [0] * (N+M+1)

    for n in arr_N:
        for m in arr_M:
            cnt[n+m] += 1

    max_v = max(cnt)
    ans = []
    for i in range(len(cnt)):
        if cnt[i] == max_v:
            ans.append(i)

    print(*ans)