import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    note1 = set(map(int, input().split()))  # 중복 제거
    M = int(input())
    note2 = list(map(int, input().split()))

    for n2 in note2:
        if n2 in note1:
            print(1)
        else:
            print(0)



''' [시간초과]
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    note1 = list(map(int, input().split()))
    M = int(input())
    note2 = list(map(int, input().split()))

    for n2 in note2:
        if n2 in note1:
            print(1)
        else:
            print(0)
'''



''' [시간초과]
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    note1 = list(map(int, input().split()))
    M = int(input())
    note2 = list(map(int, input().split()))

    note1.sort()

    for n2 in note2:
        l = 0
        r = N-1
        check = 0
        while l <= r:
            m = (l+r)//2
            if n2 == note1[m]:
                check = 1
                break
            elif n2 > note1[m]:
                l = m+1
            else:
                r = m-1

        print(check)
'''