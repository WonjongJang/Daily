import sys
sys.stdin = open('input.txt')

tc = 0
while True:
    tc += 1
    L, P, V = map(int, input().split()) # 연속하는 P일 중 L일 동안 캠핑장 사용 가능, V일 휴가

    if L == 0 and P == 0 and V == 0:
        break

    ans = L * (V // P)
    if L >= (V % P):
        ans += (V % P)
    else:
        ans += L

    print('Case {}: {}'.format(tc, ans))