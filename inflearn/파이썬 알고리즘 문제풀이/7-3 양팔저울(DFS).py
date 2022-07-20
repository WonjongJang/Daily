import sys
sys.stdin = open('7-3 input.txt')


def recur(sum, cnt):
    if cnt == K:
        tmp = abs(sum)
        if sum and not v[tmp]:
            v[tmp] = 1
        return

    recur(sum + K_list[cnt], cnt+1)
    recur(sum - K_list[cnt], cnt+1)
    recur(sum, cnt+1)

# 전체 반복 횟수
T = int(input())

# 전체 반복
for tc in range(1, T+1):
    K = int(input())
    K_list = list(map(int, input().split()))

    S = sum(K_list)
    S_list = list(range(1, S+1))
    v = [0] * (S+1)

    recur(0, 0)

    print(v[1:].count(0))



''' [풀이]
def DFS(L, sum):
    global res
    if L==n:
        if 0<sum<=s:
            res.add(sum)
    else:
        DFS(L+1, sum+G[L])
        DFS(L+1, sum-G[L])
        DFS(L+1, sum)

n=int(input())
G=list(map(int, input().split()))
s=sum(G)
res=set()
DFS(0, 0)
print(s-len(res))
'''