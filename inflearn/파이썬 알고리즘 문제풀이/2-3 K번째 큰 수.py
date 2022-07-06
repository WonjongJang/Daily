import sys
sys.stdin = open('1-3 input.txt', 'rt')


# 전체 반복 횟수
T = int(input())

# 전체 반복
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))

    tmp = set()

    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                tmp.add(arr[i] + arr[j] + arr[k])

    ans = list(tmp)
    ans.sort(reverse=True)

    print(ans[K-1])