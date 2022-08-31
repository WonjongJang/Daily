import sys
sys.stdin = open('7-8 input.txt')


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]


    v = [[0]*N for _ in range(N)]
    s = N//2
    q = []
    q.append((s, s))
    v[s][s] = 1
    ans = data[s][s]

    cur = 0
    while q:
        if cur == s:
            break

        size = len(q)
        for _ in range(size):
            x, y = q.pop(0)
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if not v[nx][ny]:
                    q.append((nx, ny))
                    v[nx][ny] = 1
                    ans += data[nx][ny]
        cur += 1

    print(ans)



''' [풀이]
import sys
from collections import deque
sys.stdin=open("input.txt", "r")
dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]
n=int(input())
a=[list(map(int, input().split())) for _ in range(n)]
ch=[[0]*n for _ in range(n)]
sum=0
Q=deque()
ch[n//2][n//2]=1
sum+=a[n//2][n//2]
Q.append((n//2, n//2))
L=0
while True:
    if L==n//2:
        break
    size=len(Q)
    for i in range(size):
        tmp=Q.popleft()
        for j in range(4):
            x=tmp[0]+dx[j]
            y=tmp[1]+dy[j]
            if ch[x][y]==0:
                sum+=a[x][y]
                ch[x][y]=1
                Q.append((x, y))
    L+=1
print(sum)
    

'''