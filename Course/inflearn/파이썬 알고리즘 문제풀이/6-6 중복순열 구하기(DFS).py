import sys
sys.stdin = open('6-6 input.txt', 'rt')


def recur(n, r, cnt):
    global sum

    if cnt == r:
        print(*p)
        sum += 1
    else:
        for i in range(n):
            p[cnt] = i+1
            recur(n, r, cnt+1)

# 전체 반복 횟수
T = int(input())

# 전체 반복
for tc in range(1, T+1):
    N, M = map(int, input().split())

    p = [0] * M
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
            res[L]=i
            DFS(L+1)

n, m=map(int, input().split())
res=[0]*n
cnt=0
DFS(0)
print(cnt)
'''