import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    P = [0, 1, 1, 1]

    if N == 1 or N == 2 or N == 3:
        ans = P[N]
    else:
        n = 4
        while True:
            if n > N:
                break

            P_new = P[n-3] + P[n-2]
            P.append(P_new)

            n += 1
        ans= P[N]

    print(ans)