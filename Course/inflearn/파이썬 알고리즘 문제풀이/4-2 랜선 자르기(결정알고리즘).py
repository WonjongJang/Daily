import sys
sys.stdin = open('4-2 input.txt', 'rt')


# 전체 반복 횟수
T = int(input())

# 전체 반복
for tc in range(1, T+1):
    K, N = map(int, input().split())
    arr = [int(input()) for _ in range(K)]

    l = 1
    r = max(arr)
    ans = 0
    while l <= r:
        m = (l+r) // 2
        cnt = 0
        for i in range(len(arr)):
            cnt += arr[i] // m

        if cnt >= N:
            ans = m
            l = m+1
        elif cnt < N:
            r = m-1

    print(ans)



''' [풀이]
def Count(len):
    cnt=0
    for x in Line:
        cnt+=(x//len)
    return cnt

k, n=map(int, input().split())
Line=[]
res=0
largest=0
for i in range(k):
    tmp=int(input())
    Line.append(tmp)
    largest=max(largest, tmp)
lt=1
rt=largest
while lt<=rt:
    mid=(lt+rt)//2
    if Count(mid)>=n:
        res=mid
        lt=mid+1
    else:
        rt=mid-1
print(res)
'''