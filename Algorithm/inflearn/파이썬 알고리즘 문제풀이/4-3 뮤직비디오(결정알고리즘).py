import sys
sys.stdin = open('4-3 input.txt', 'rt')


# 전체 반복 횟수
T = int(input())

# 전체 반복
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    max_v = max(arr)

    l = 1
    r = sum(arr)
    ans = 0
    while l <= r:
        m = (l+r) // 2

        cnt = 1
        tmp = 0
        for i in range(N):
            if tmp + arr[i] > m:
                cnt += 1
                tmp = arr[i]
            else:
                tmp += arr[i]

        if m >= max_v and cnt <= M:
            ans = m
            r = m-1
        else:
            l = m+1

    print(ans)



''' [풀이]
def Count(capacity):
    cnt=1
    sum=0
    for x in Music:
        if sum+x>capacity:
            cnt+=1
            sum=x
        else:
            sum+=x
    return cnt

n, m=map(int, input().split())
Music=list(map(int, input().split()))
maxx=max(Music)
lt=1
rt=sum(Music)
res=0
while lt<=rt:
    mid=(lt+rt)//2
    if mid>=maxx and Count(mid)<=m:
        res=mid
        rt=mid-1
    else:
        lt=mid+1
print(res)
'''