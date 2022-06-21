import sys
sys.stdin = open('3-10 input.txt', 'rt')


def checkThree(x, y):
    check = [0] * 10
    for i in range(x, x+3):
        for j in range(y, y+3):
            check[arr[i][j]] += 1

    if 0 in check[1:]:
        return 0
    else:
        return 1

# 전체 반복 횟수
T = int(input())

# 전체 반복
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    flag = 1
    for x in range(9):
        check_r = [0] * 10
        check_c = [0] * 10
        check_t = 1
        for y in range(9):
            if not x%3 and not y%3:
                check_t = checkThree(x, y)
            check_r[arr[x][y]] += 1
            check_c[arr[y][x]] += 1

        if 0 in check_r[1:] or 0 in check_c[1:] or not check_t:
            flag = 0
            break

    if flag:
        print("YES")
    else:
        print("NO")




''' [풀이]
def check(a):
    for i in range(9):
        ch1=[0]*10
        ch2=[0]*10
        for j in range(9):
            ch1[a[i][j]]=1
            ch2[a[j][i]]=1
        if sum(ch1)!=9 or sum(ch2)!=9:
            return False
    for i in range(3):
        for j in range(3):
            ch3=[0]*10
            for k in range(3):
                for s in range(3):
                    ch3[a[i*3+k][j*3+s]]=1
            if sum(ch3)!=9:
                return False
    return True

a=[list(map(int, input().split())) for _ in range(9)]
if check(a):
    print("YES")
else:
    print("NO")
'''