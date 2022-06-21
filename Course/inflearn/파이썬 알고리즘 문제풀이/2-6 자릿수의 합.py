import sys
sys.stdin = open('1-6 input.txt', 'rt')

def digit_sum(x):
    sum = 0
    for i in x:
        sum += int(i)
    return sum

# 전체 반복 횟수
T = int(input())

# 전체 반복
for tc in range(1, T+1):
    N = int(input())    # 자연수의 개수
    arr = list(input().split())

    max_v = 0
    ans = 0
    for a in arr:
        tmp = digit_sum(a)
        if tmp > max_v:
            max_v = tmp
            ans = a

    print(ans)