import sys
sys.stdin = open('6-9 input.txt', 'rt')


def recur(n, r, cnt):
    global ans
    if ans:
        return

    if cnt == r:
        arr = p[::]
        while len(arr) > 1:
            tmp = []
            for i in range(len(arr)-1):
                tmp.append(arr[i] + arr[i+1])
            arr = tmp[::]
        if arr[0] == F:
            ans = p[::]
            return
    else:
        for i in range(1, n+1):
            if not v[i]:
                v[i] = 1
                p[cnt] = i
                recur(n, r, cnt+1)
                v[i] = 0

# 전체 반복 횟수
T = int(input())

# 전체 반복
for tc in range(1, T+1):
    N, F = map(int, input().split())

    p = [0] * N
    v = [0] * (N+1)

    ans = []
    recur(N, N, 0)

    print(*ans)



''' [풀이]
def DFS(L, sum):
    if L==n and sum==f:
        for x in p:
            print(x, end=' ')
        sys.exit(0)
    else:
        for i in range(1, n+1):
            if ch[i]==0:
                ch[i]=1
                p[L]=i
                DFS(L+1, sum+(p[L]*b[L]))
                ch[i]=0

n, f=map(int, input().split())
p=[0]*n
b=[1]*n
ch=[0]*(n+1)
for i in range(1, n):
    b[i]=b[i-1]*(n-i)//i
DFS(0, 0)
'''

''' [풀이(라이브러리)]
import itertools as it

n, f=map(int, input().split())
b=[1]*n
cnt=0
for i in range(1, n):
    b[i]=b[i-1]*(n-i)/i
a=list(range(1, n+1))
for tmp in it.permutations(a):
    sum=0
    for L, x in enumerate(tmp):
        sum+=(x*b[L])
    if sum==f:
        for x in tmp:
            print(x, end=' ')
        break
'''