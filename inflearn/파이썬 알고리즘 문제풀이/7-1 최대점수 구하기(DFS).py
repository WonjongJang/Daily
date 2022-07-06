import sys
sys.stdin = open('7-1 input.txt', 'rt')


def recur(x, limit, tot):
    global max_v

    if x == N:
        if limit <= M:
            max_v = max(max_v, tot)
    else:
        recur(x+1, limit+arr[x][1], tot+arr[x][0])
        recur(x+1, limit, tot)

# 전체 반복 횟수
T = int(input())

# 전체 반복
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_v = 0

    recur(0, 0, 0)

    print(max_v)



''' [풀이]
def DFS(L, sum, time):
    global res
    if time>m:
        return
    if L==n:
        if sum>res:
            res=sum
    else:
        DFS(L+1, sum+pv[L], time+pt[L])
        DFS(L+1, sum, time)

n, m=map(int, input().split())
pv=list()
pt=list()
for i in range(n):
    a, b=map(int, input().split())
    pv.append(a)
    pt.append(b)
res=-2147000000
DFS(0, 0, 0)
print(res)
'''