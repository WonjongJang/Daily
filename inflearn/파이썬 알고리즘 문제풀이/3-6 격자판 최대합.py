import sys
sys.stdin = open('3-6 input.txt', 'rt')


# 전체 반복 횟수
T = int(input())

# 전체 반복
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_v = 0
    sum_d1 = sum_d2 = 0
    for x in range(N):
        sum_row = 0
        sum_col = 0
        sum_d1 += arr[x][x]
        sum_d2 += arr[x][x]
        for y in range(N):
            sum_row += arr[x][y]
            sum_col += arr[y][x]
        max_v = max(max_v, sum_row, sum_col)

    max_v = max(max_v, sum_d1, sum_d2)

    print(max_v)



''' [풀이]
n=int(input())
a=[list(map(int, input().split())) for _ in range(n)]
largest=-2147000000
for i in range(n):
    sum1=sum2=0
    for j in range(n):
        sum1+=a[i][j]
        sum2+=a[j][i]
    if sum1>largest:
        largest=sum1
    if sum2>largest:
        largest=sum2
sum1=sum2=0
for i in range(n):
    sum1+=a[i][i]
    sum2+=a[i][n-i-1]
if sum1>largest:
    largest=sum1
if sum2>largest:
    largest=sum2
print(largest)
'''