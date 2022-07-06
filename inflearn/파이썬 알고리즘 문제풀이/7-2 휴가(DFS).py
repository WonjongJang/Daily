import sys
sys.stdin = open('7-2 input.txt', 'rt')


def recur(x, tot):
    global max_v

    if x == N+1:
        max_v = max(max_v, tot)
    else:
        if x+arr[x][0] <= N+1:
            recur(x+arr[x][0], tot+arr[x][1])
        recur(x+1, tot)

# 전체 반복 횟수
T = int(input())

# 전체 반복
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr.insert(0, [0, 0])

    max_v = 0
    recur(1, 0)

    print(max_v)



''' [풀이]
def DFS(L, sum):
    global res
    if L==n+1:
        if sum>res:
            res=sum
    else:
        if L+T[L]<=n+1:
            DFS(L+T[L], sum+P[L])
        DFS(L+1, sum)

n=int(input())
T=list()
P=list()
for i in range(n):
    a, b=map(int, input().split())
    T.append(a)
    P.append(b)
res=-2147000000
T.insert(0, 0)
P.insert(0, 0)
DFS(1, 0)
print(res)
'''