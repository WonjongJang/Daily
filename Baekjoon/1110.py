N = input()    # 0 <= N <= 99 정수

if int(N) < 10:
    N = '0' + N

ans = N
cnt = 0
while True:
    sum = str(int(N[0]) + int(N[1]))
    if len(sum) == 1:
        sum = '0' + sum

    N = N[1] + sum[1]
    cnt += 1

    if N == ans:
        break

print(cnt)