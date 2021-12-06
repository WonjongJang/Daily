import sys
sys.stdin = open('input.txt')

bin_straw = [
    0,
    'VVV딸기',
    'VV딸기V',
    'VV딸기딸기',
    'V딸기VV',
    'V딸기V딸기',
    'V딸기딸기V',
    'V딸기딸기딸기',
    '딸기VVV',
    '딸기VV딸기',
    '딸기V딸기V',
    '딸기V딸기딸기',
    '딸기딸기VV',
    '딸기딸기V딸기',
    '딸기딸기딸기V',
    '딸기딸기딸기딸기'
]

# 전체 반복 횟수
T = int(input())

# 전체 반복
for tc in range(1, T+1):
    N = int(input())

    if N > 15:
        # print(N)
        N = N - 15
        quo, rem = N//14, N%14
        # print(quo, rem)
        if quo % 2:
            N = 1 + rem
        else:
            N = 15 - rem

    # print(N)
    print(bin_straw[N])
    # print()