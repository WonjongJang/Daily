import sys
sys.stdin = open('6-11 input.txt', 'rt')


def recur(n, r, s, cnt):
    global ans

    if cnt == r:
        if not sum(c) % M:
            ans += 1
    else:
        for i in range(s, n-r+cnt+1):
            c[cnt] = arr[i]
            recur(n, r, i+1, cnt+1)

# 전체 반복 횟수
T = int(input())

# 전체 반복
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    M = int(input())

    c = [0] * K

    ans = 0
    recur(N, K, 0, 0)

    print(ans)



''' [풀이]
def DFS(L, s, sum):
    global cnt
    if L==k:
        if sum%m==0:
            cnt+=1
    else:
        for i in range(s, n):
            DFS(L+1, i+1, sum+a[i])
 
n, k=map(int, input().split())
a=list(map(int, input().split()))
m=int(input())
cnt=0
DFS(0, 0, 0)
print(cnt)
'''

''' [풀이(라이브러리)]
import itertools as it

n, k=map(int, input().split())
a=list(map(int, input().split()))
m=int(input())
cnt=0
for x in it.combinations(a, k):
    if sum(x)%m==0:
        cnt+=1
print(cnt)
'''