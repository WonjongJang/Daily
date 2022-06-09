import sys
sys.stdin = open('1-2 input.txt', 'rt')


# 전체 반복 횟수
T = int(input())

# 전체 반복
for tc in range(1, T+1):
    N, s, e, k = map(int, input().split())
    arr = list(map(int, input().split()))

    ans = arr[s-1:e]
    ans.sort()

    print('#{} {}'.format(tc, ans[k-1]))