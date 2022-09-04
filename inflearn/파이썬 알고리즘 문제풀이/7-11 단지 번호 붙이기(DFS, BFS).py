import sys
sys.stdin = open('7-11 input.txt')


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def recur(x, y):
    que = []
    que.append((x, y))
    data[x][y] = 0
    cnt = 1

    while que:
        x, y = que.pop(0)

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < N and data[nx][ny]:
                data[nx][ny] = 0
                que.append((nx, ny))
                cnt += 1

    ans.append(cnt)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input())) for _ in range(N)]

    ans = []
    for x in range(N):
        for y in range(N):
            if data[x][y]:
                recur(x, y)

    ans.sort()
    print(len(ans))
    for i in ans:
        print(i)



''' [풀이] DFS
import sys
sys.stdin=open("input.txt", "r")
dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]

def DFS(x, y):
    global cnt
    cnt+=1
    board[x][y]=0
    for i in range(4):
        xx=x+dx[i]
        yy=y+dy[i]
        if 0<=xx<n and 0<=yy<n and board[xx][yy]==1:
            DFS(xx, yy)

if __name__=="__main__":
    n=int(input())
    board=[list(map(int, input())) for _ in range(n)]
    res=[]
    for i in range(n):
        for j in range(n):
            if board[i][j]==1:
                cnt=0
                DFS(i, j)
                res.append(cnt)
    print(len(res))
    res.sort()
    for x in res:
        print(x)
'''

''' [풀이] DFS
import sys
from collections import deque
sys.stdin=open("input.txt", "r")
dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]
n=int(input())
board=[list(map(int, input())) for _ in range(n)]
cnt=0
res=[]
Q=deque()
for i in range(n):
    for j in range(n):
        if board[i][j]==1:
            board[i][j]=0
            Q.append((i, j))
            cnt=1
            while Q:
                tmp=Q.popleft()
                for k in range(4):
                    x=tmp[0]+dx[k]
                    y=tmp[1]+dy[k]
                    if x<0 or x>=n or y<0 or y>=n or board[x][y]==0:
                        continue
                    board[x][y]=0
                    Q.append((x, y))
                    cnt+=1
            res.append(cnt)

print(len(res))
res.sort()
for x in res:
    print(x)
'''