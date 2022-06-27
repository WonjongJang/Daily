import sys
sys.stdin = open('6-15 input.txt', 'rt')


def recur(s):
    global ans

    if s == N:
        ans += 1
    else:
        for i in range(1, N+1):
            if v[i] == 0 and adj[s][i]:
                v[i] = 1
                recur(i)
                v[i] = 0

# 전체 반복 횟수
T = int(input())

# 전체 반복
for tc in range(1, T+1):
    N, M = map(int, input().split())

    adj = [[0] * (N+1) for _ in range(N+1)]
    v = [0] * (N+1)

    for i in range(M):
        s, e = map(int, input().split())
        adj[s][e] = 1

    ans = 0
    v[1] = 1
    recur(1)

    print(ans)



''' [풀이]
def DFS(v):
    global cnt, path
    if v==n:
        cnt+=1
        for x in path:
            print(x, end=' ')
        print()
    else:
        for i in range(1, n+1):
            if g[v][i]==1 and ch[i]==0:
                ch[i]=1
                path.append(i)
                DFS(i)
                path.pop()
                ch[i]=0
           
n, m=map(int, input().split())
g=[[0]*(n+1) for _ in range(n+1)]
ch=[0]*(n+1)
for i in range(m):
    a, b=map(int, input().split())
    g[a][b]=1
cnt=0
ch[1]=1
path=list()
path.append(1)
DFS(1)
print(cnt)
'''