import sys
sys.stdin = open('6-8 input.txt', 'rt')


def recur(n, r, cnt):
    global sum

    if cnt == r:
        print(*p)
        sum += 1
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
    N, M = map(int, input().split())

    p = [0] * M
    v = [0] * (N+1)

    sum = 0
    recur(N, M, 0)

    print(sum)



''' [풀이]
def DFS(L):
    global cnt
    if L==m:
        for i in range(m):
            print(res[i], end=' ')
        print()
        cnt+=1
    else:
        for i in range(1, n+1):
            if ch[i]==0:
                ch[i]=1
                res[L]=i
                DFS(L+1)
                ch[i]=0

if __name__=="__main__":
    n, m=map(int, input().split())
    res=[0]*n
    ch=[0]*(n+1)
    cnt=0
    DFS(0)
    print(cnt)
'''