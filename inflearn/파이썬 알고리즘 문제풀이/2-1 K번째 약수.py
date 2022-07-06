import sys
sys.stdin = open('1-1 input.txt', 'rt')


# 전체 반복 횟수
T = 6

# 전체 반복
for tc in range(1, T+1):
    N, K = map(int, input().split())

    cnt = 0
    ans = 0
    for i in range(1, N+1):
        if not N%i:
            cnt += 1
            if cnt == K:
                ans = i
                break
    else:
        ans = -1

    print(ans)