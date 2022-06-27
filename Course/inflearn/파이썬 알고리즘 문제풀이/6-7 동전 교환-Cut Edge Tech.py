import sys
sys.stdin = open('6-7 input.txt', 'rt')


def recur(cnt, sum):
    global min_v
    if cnt > min_v:
        return
    if sum > M:
        return
    if sum == M:
        min_v = min(min_v, cnt)
    else:
        for i in range(N):
            recur(cnt+1, sum+arr[i])

# 전체 반복 횟수
T = int(input())

# 전체 반복
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    M = int(input())

    arr.sort(reverse=True)

    min_v = 2147000000
    recur(0, 0)

    print(min_v)

    # [잘못된 예시]
    # cnt = 0
    #
    # for i in range(N):
    #     while True:
    #         if M - type[i] >= 0:
    #             M -= type[i]
    #             cnt += 1
    #         else:
    #             break
    #
    # print(cnt)



''' [풀이]
def DFS(L, sum):
    global res
    if L>=res:
        return
    if sum>m:
        return
    if sum==m:
        if L<res:
            res=L
    else:
        for i in range(n):
            DFS(L+1, sum+a[i])

n=int(input())
a=list(map(int, input().split()))
m=int(input())
res=2147000000
a.sort(reverse=True)
DFS(0, 0)
print(res)
'''