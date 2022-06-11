import sys
sys.stdin = open('4-4 input.txt', 'rt')


# 전체 반복 횟수
T = int(input())

# 전체 반복
for tc in range(1, T+1):
    N, C = map(int, input().split())    # N: 마구간 개수, C: 말의 수
    arr = [int(input()) for _ in range(N)]

    arr.sort()

    ans = 0
    l = 1
    r = arr[-1]
    while l <= r:
        mid = (l+r) // 2

        cnt = 1
        ep = arr[0]
        for i in range(1, N):
            if arr[i]-ep >= mid:
                cnt += 1
                ep = arr[i]

        if cnt >= C:
            ans = mid
            l = mid+1
        else:
            r = mid-1

    print(ans)



''' [풀이]
def Count(len):
    cnt=1
    ep=Line[0]
    for i in range(1, n):
        if Line[i]-ep>=len:
            cnt+=1
            ep=Line[i]
    return cnt

n, c=map(int, input().split())
Line=[]
for _ in range(n):
    tmp=int(input())
    Line.append(tmp)
Line.sort()
lt=1
rt=Line[n-1]
while lt<=rt:
    mid=(lt+rt)//2
    if Count(mid)>=c:
        res=mid
        lt=mid+1
    else:
        rt=mid-1

print(res)
'''