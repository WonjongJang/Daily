import sys
sys.stdin = open('1-8 input.txt', 'rt')


def isPrime(x):
    if x == 1:          # 1이면 (1은 소수가 아님)
        return          # 탈출

    for i in range(2, x):
        if i*i > x:
            break

        if not x % i:   # 소수가 아니면
            return      # 탈출

    ans.append(x)


def reverse(x):
    tmp = list(str(x))
    rev_num = ''

    while tmp:
        rev_num += tmp.pop()

    isPrime(int(rev_num))

# 전체 반복 횟수
T = int(input())

# 전체 반복
for tc in range(1, T+1):
    N = int(input())    # 자연수의 개수
    arr = list(map(int, input().split()))

    ans = []

    for i in range(N):
        reverse(arr[i])

    print(*ans)