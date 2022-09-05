import sys
sys.stdin = open('7-12 input.txt')


dx = [-1, 0, 1, 0, -1, -1, 1, 1]
dy = [0, 1, 0, -1, -1, 1, -1, 1]

def bfs(x, y):
    que = []
    que.append((x, y))
    data[x][y] = 0

    while que:
        x, y = que.pop(0)

        for d in range(8):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < N and data[nx][ny]:
                que.append((nx, ny))
                data[nx][ny] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0
    for x in range(N):
        for y in range(N):
            if data[x][y]:
                cnt += 1
                bfs(x, y)

    print(cnt)



''' [풀이]
import sys
from collections import deque
sys.stdin=open("input.txt", "r")
dx=[-1, -1, 0, 1, 1, 1, 0, -1]
dy=[0, 1, 1, 1, 0, -1, -1, -1]
n=int(input())
board=[list(map(int, input().split())) for _ in range(n)]
cnt=0
Q=deque()
for i in range(n):
    for j in range(n):
        if board[i][j]==1:
            board[i][j]=0
            Q.append((i, j))
            while Q:
                tmp=Q.popleft()
                for k in range(8):
                    x=tmp[0]+dx[k]
                    y=tmp[1]+dy[k]
                    if 0<=x<n and 0<=y<n and board[x][y]==1:
                        board[x][y]=0
                        Q.append((x, y))
            cnt+=1
print(cnt)

'''