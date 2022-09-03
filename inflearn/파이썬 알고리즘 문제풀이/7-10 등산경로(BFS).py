import sys
sys.stdin = open('7-10 input.txt')


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]

    start = [data[0][0], (0, 0)]
    end = [data[0][0], (0, 0)]
    for x in range(N):
        for y in range(N):
            if start[0] > data[x][y]:
                start[0] = data[x][y]
                start[1] = (x, y)
            if end[0] < data[x][y]:
                end[0] = data[x][y]
                end[1] = (x, y)

    ans = 0
    que = []
    que.append(start[1])
    while que:
        x, y = que.pop(0)

        if x == end[1][0] and y == end[1][1]:
            ans += 1

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < N and data[x][y] < data[nx][ny]:
                que.append((nx, ny))

    print(ans)



''' [풀이]
import sys
sys.stdin=open("input.txt", "r")
dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]

def DFS(x, y):
    global cnt
    if x==ex and y==ey:
        cnt+=1
    else:
        for k in range(4):
            xx=x+dx[k]
            yy=y+dy[k]
            if 0<=xx<n and 0<=yy<n and ch[xx][yy]==0 and board[xx][yy]>board[x][y]:
                ch[xx][yy]=1
                DFS(xx, yy)
                ch[xx][yy]=0

if __name__=="__main__":
    n=int(input())
    board=[[0]*n for _ in range(n)]
    ch=[[0]*n for _ in range(n)]
    max=-2147000000
    min=2147000000
    for i in range(n):
        tmp=list(map(int, input().split()))
        for j in range(n):
            if tmp[j]<min:
                min=tmp[j]
                sx=i
                sy=j
            if tmp[j]>max:
                max=tmp[j]
                ex=i
                ey=j      
            board[i][j]=tmp[j]
    ch[sx][sy]=1
    cnt=0
    DFS(sx, sy)
    print(cnt)
'''