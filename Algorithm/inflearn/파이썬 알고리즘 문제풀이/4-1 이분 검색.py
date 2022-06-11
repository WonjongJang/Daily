import sys
sys.stdin = open('4-1 input.txt', 'rt')


# 전체 반복 횟수
T = int(input())

# 전체 반복
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    arr.sort()

    ans = 0
    l = 0
    r = N-1
    while l <= r:
        m = (l+r) // 2
        if arr[m] == M:
            ans = m
            break
        elif arr[m] > M:
            r = m-1
        else:
            l = m+1

    print(ans+1)



''' [풀이]
n, m=map(int, input().split())
a=list(map(int, input().split()))
a.sort()
lt=0
rt=n-1
while lt<=rt:
    mid=(lt+rt)//2
    if a[mid]==m:
        print(mid+1)
        break
    elif a[mid]>m:
        rt=mid-1
    else:
        lt=mid+1
'''