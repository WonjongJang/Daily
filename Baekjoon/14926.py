import sys
sys.setrecursionlimit(10**6)


def recur(n):
    ans.append('a' + str(n))

    for i in range(1, N+1):
        if not ch[n][i] and not ch[i][n]:
            ch[i][n] = 1
            recur(i)

N = int(input())
ch = [[0]*(N+1) for _ in range(N+1)]

for i in range(1, N+1): # 자기자신 못가도록 초기화
    ch[i][i] = 1

ch[1][N] = 1    # 시작 노드는 마지막에 추가할 것

ans = []
recur(1)

ans.append('a1')    # 시작 노드 추가
print(*ans)