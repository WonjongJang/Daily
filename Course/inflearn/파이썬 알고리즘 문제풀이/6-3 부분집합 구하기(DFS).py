import sys
sys.stdin = open('6-3 input.txt', 'rt')


def recur(x):
    if x == N+1:
        for i in range(1, len(V)):
            if V[i]:
                print(i, end=' ')
        print()
    else:
        V[x] = 1
        recur(x+1)
        V[x] = 0
        recur(x+1)

# 전체 반복 횟수
T = int(input())

# 전체 반복
for tc in range(1, T+1):
    N = int(input())
    V = [0] * (N+1)

    recur(1)



''' [풀이]
def DFS(v):
    if v==n+1:
        for i in range(1, n+1):
            if ch[i]==1:
                print(i, end=' ')
        print()
    else:
        ch[v]=1
        DFS(v+1)
        ch[v]=0
        DFS(v+1)

n=int(input())
ch=[0]*(n+1)
DFS(1)
'''