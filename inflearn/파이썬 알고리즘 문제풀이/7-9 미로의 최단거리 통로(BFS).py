import sys
sys.stdin = open('7-9 input.txt')


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

T = int(input())
for tc in range(1, T+1):
    data = [list(map(int, input().split())) for _ in range(7)]

    v = [[-1]*7 for _ in range(7)]

    que = []
    que.append((0, 0))
    v[0][0] = 0

    while que:
        x, y = que.pop(0)

        if x == 6 and y == 6:
            break

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < 7 and 0 <= ny < 7 and not data[nx][ny] and v[nx][ny] == -1:
                que.append((nx, ny))
                v[nx][ny] = v[x][y] + 1

    print(v[6][6])



''' [풀이]
import sys
from collections import deque
sys.stdin=open("input.txt", "r")
dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]
board=[list(map(int, input().split())) for _ in range(7)]
dis=[[0]*7 for _ in range(7)]
Q=deque()
Q.append((0, 0))
board[0][0]=1
while Q:
    tmp=Q.popleft()
    for i in range(4):
        x=tmp[0]+dx[i]
        y=tmp[1]+dy[i]
        if 0<=x<=6 and 0<=y<=6 and board[x][y]==0:
            board[x][y]=1
            dis[x][y]=dis[tmp[0]][tmp[1]]+1
            Q.append((x, y))
if dis[6][6]==0:
    print(-1)
else:
    print(dis[6][6])
'''