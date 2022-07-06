import sys
sys.stdin = open('6-5 input.txt', 'rt')


def recur(x, sum, tsum):
    global max_v

    if sum + (tot-tsum) < max_v:
        return

    if sum > C:
        return

    if x == N:
        max_v = max(max_v, sum)
    else:
        recur(x+1, sum+arr[x], tsum+arr[x])
        recur(x+1, sum, tsum+arr[x])

# 전체 반복 횟수
T = int(input())

# 전체 반복
for tc in range(1, T+1):
    C, N = map(int, input().split())
    arr = [int(input()) for _ in range(N)]

    tot = sum(arr)
    max_v = 0

    recur(0, 0, 0)

    print(max_v)



''' [풀이]
def DFS(L, sum, tsum):
    global result
    if sum+(total-tsum)<result:
        return
    if sum>c:
        return
    if L==n:
        if sum>result:
            result=sum
    else:
        DFS(L+1, sum+a[L], tsum+a[L])
        DFS(L+1, sum, tsum+a[L])

c, n=map(int, input().split())
a=[0]*n
result=-2147000000
for i in range(n):
    a[i]=int(input())
total=sum(a)
DFS(0, 0, 0)
print(result)
'''