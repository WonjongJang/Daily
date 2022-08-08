import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort(reverse=True)
    B.sort(reverse=True)

    cnt = 0
    a = b = 0
    while a < N and b < M:
        if A[a] > B[b]:
            cnt += (M-b)
            a += 1
        else:
            b += 1

    print(cnt)



''' [시간초과]
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort(reverse=True)
    B.sort(reverse=True)

    cnt = 0
    for a in A:
        for b in B:
            if a > b:
                cnt += 1

    print(cnt)
'''