import sys
sys.stdin = open('6-10 input.txt', 'rt')


def recur(n, r, s, cnt):
    global sum

    if cnt == r:
        print(*c)
        sum += 1
    else:
        for i in range(s, n-r+cnt+1):
            c[cnt] = i+1
            recur(n, r, i+1, cnt+1)

# 전체 반복 횟수
T = int(input())

# 전체 반복
for tc in range(1, T+1):
    N, M = map(int, input().split())

    sum = 0
    c = [0] * M

    recur(N, M, 0, 0)

    print(sum)



''' [풀이]
def DFS(L, s):
    global cnt
    if L==m:
        for i in range(m):
            print(res[i], end=' ')
        print()
        cnt+=1
    else:
        for i in range(s, n+1):
            res[L]=i
            DFS(L+1, i+1)
           
n, m=map(int, input().split())
res=[0]*(n+1)
cnt=0
DFS(0, 1)
print(cnt)
'''