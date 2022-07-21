import sys
sys.stdin = open('7-4 input.txt')


def recur(L, sum):
    global ans

    if sum > T:
        return
    if L == K:
        if sum == T:
            ans += 1
    else:
        for i in range(C[L][1]+1):
            recur(L+1, sum+(C[L][0]*i))

TC = int(input())
for _ in range(TC):
    T = int(input())
    K = int(input())
    C = []
    for _ in range(K):
        c, n = map(int, input().split())
        C.append([c, n])

    ans = 0
    recur(0, 0)

    print(ans)



''' [풀이]
def DFS(L, sum):
    global cnt
    if sum>m:
        return
    if L==n:
        if sum==m:
            cnt+=1
    else:
        for i in range(cn[L]+1):
            DFS(L+1, sum+(cv[L]*i))

m=int(input())
n=int(input())
cv=list()
cn=list()
for i in range(n):
    a, b=map(int, input().split())
    cv.append(a)
    cn.append(b)
cnt=0
DFS(0, 0)
print(cnt)
'''