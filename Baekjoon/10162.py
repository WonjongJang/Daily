T = int(input())

A = 300
B = 60
C = 10

cnt_a = cnt_b = cnt_c = fail = 0   # A, B, C 사용 횟수

while True:
    if T - A > 0:
        T -= A
        cnt_a += 1
    elif T - A == 0:
        T -= A
        cnt_a += 1
        break
    else:
        if T - B > 0:
            T -= B
            cnt_b += 1
        elif T - B == 0:
            T -= B
            cnt_b += 1
            break
        else:
            if T - C > 0:
                T -= C
                cnt_c += 1
            elif T - C == 0:
                T -= C
                cnt_c += 1
                break
            else:
                fail = -1
                break
    
if fail == 0:
    print(cnt_a, cnt_b, cnt_c)
else:
    print(fail)