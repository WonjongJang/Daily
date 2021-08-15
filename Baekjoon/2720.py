import sys
sys.stdin = open('input.txt')

def change(C, type):
    i = 0
    while True:
        if round(C, 2) > round((i+1)*type, 2):
            i += 1
        elif round(C, 2) == round((i+1)*type, 2):
            i += 1
            return i
        else:
            return i

T = int(input())

for tc in range(1, T+1):
    C = int(input())
    C = C / 100

    # 거스름돈
    Q = 0.25
    D = 0.10
    N = 0.05
    P = 0.01    

    Q_i = change(C, Q)
    C = C - (Q * Q_i)
    D_i = change(C, D)
    C = C - (D * D_i)
    N_i = change(C, N)
    C = C - (N * N_i)
    P_i = change(C, P)
    C = C - (P * P_i)

    print(Q_i, D_i, N_i, P_i)