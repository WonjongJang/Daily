import sys
sys.stdin = open('3-5 input.txt', 'rt')


# 전체 반복 횟수
T = int(input())

# 전체 반복
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    cnt = 0
    for i in range(N):
        sum = 0
        if arr[i] == M:
            cnt += 1
        elif arr[i] < M and i != N-1:
            sum += arr[i]
            tmp = i
            while tmp != N-1:
                tmp += 1
                sum += arr[tmp]
                if sum == M:
                    cnt += 1
                    break
                elif sum > M:
                    break

    print(cnt)



''' [풀이]
n, m=map(int, input().split())
a=list(map(int, input().split()))
lt=0
rt=1
tot=a[0]
cnt=0
while True:
    if tot<m:
        if rt<n:
            tot+=a[rt]
            rt+=1
        else:
            break
    elif tot==m:
        cnt+=1
        tot-=a[lt]
        lt+=1
    else:
        tot-=a[lt]
        lt+=1
print(cnt)
'''