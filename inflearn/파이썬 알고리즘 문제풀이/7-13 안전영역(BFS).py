import sys
sys.stdin = open('7-13 input.txt')


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    que = []
    que.append((x, y))
    v[x][y] = 0

    while que:
        x, y = que.pop(0)

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < N and v[nx][ny]:
                que.append((nx, ny))
                v[nx][ny] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]

    h = 1
    max_v = 0

    while True:
        if h > 100:
            break

        v = [[0]*N for _ in range(N)]
        for x in range(N):
            for y in range(N):
                if data[x][y] > h:
                    v[x][y] = 1

        cnt = 0
        for x in range(N):
            for y in range(N):
                if v[x][y]:
                    cnt += 1
                    bfs(x, y)

        max_v = max(max_v, cnt)

        h += 1

    print(max_v)



''' [풀이]
import sys
sys.stdin=open("input.txt", "r")
dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]
sys.setrecursionlimit(10**6)
def DFS(x, y, h):
    ch[x][y]=1
    for i in range(4):
        xx=x+dx[i]
        yy=y+dy[i]
        if 0<=xx<n and 0<=yy<n and ch[xx][yy]==0 and board[xx][yy]>h:
            DFS(xx, yy, h)

if __name__=="__main__":
    n = int(input())
    cnt = 0
    res = 0
    board=[list(map(int, input().split())) for _ in range(n)]
    for h in range(100):
        ch=[[0]*n for _ in range(n)]
        cnt=0
        for i in range(n):
            for j in range(n):
                if ch[i][j]==0 and board[i][j]>h:
                    cnt+=1
                    DFS(i, j, h)
        res=max(res, cnt)
        if cnt==0:
            break
    print(res)
'''