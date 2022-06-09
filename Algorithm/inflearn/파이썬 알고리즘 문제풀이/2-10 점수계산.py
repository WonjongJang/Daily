import sys
sys.stdin = open('1-10 input.txt', 'rt')


# 전체 반복 횟수
T = int(input())

# 전체 반복
for tc in range(1, T+1):
    N = int(input())    # 문제의 개수
    arr = list(map(int, input().split()))

    flag = 0
    sum = 0
    for i in range(N):
        if arr[i]:
            if flag:
                sum += (flag+1)
                flag += 1
            else:
                sum += 1
                flag = 1
        else:
            flag = 0

    print(sum)


''' [풀이]
n=int(input())
a=list(map(int, input().split()))
cnt=0
sum=0
for i in range(n):
    if a[i]==1:
        cnt=cnt+1
        sum=sum+cnt
    else:
        cnt=0

print(sum)
'''