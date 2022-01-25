import sys
sys.stdin = open('input.txt')


N = int(input())    # 자리수

x = tmp = 15
inc = 1
cnt = 0

while len(str(tmp)) != N+1:

    inc += 1
    # print(tmp)

    if len(str(tmp)) == N:
        check = 0
        for t in str(tmp):
            if t == '1' or t == '5':
                check += 1
        if check == N:
            cnt += 1

    tmp = x * inc


# ans = cnt%1000000007
print(cnt%1000000007)