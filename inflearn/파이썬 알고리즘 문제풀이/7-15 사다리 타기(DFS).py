import sys
sys.stdin = open('7-15 input.txt')


dx = [0, 0, 1]
dy = [1, -1, 0]

def recur(x, y, s):
    global check, ans

    if not check:
        return

    v[x][y] = 1

    if x == 9:
        check = 0
        if data[x][y] == 2:
            ans = s
            return
        else:
            return

    for d in range(3):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < 10 and 0 <= ny < 10 and data[nx][ny] and not v[nx][ny]:
            recur(nx, ny, s)

T = int(input())
for tc in range(1, T+1):
    data = [list(map(int, input().split())) for _ in range(10)]

    ans = 0
    for s in range(10):
        if data[0][s]:
            v = [[0]*10 for _ in range(10)]
            check = 1
            recur(0, s, s)

    print(ans)



''' [풀이]
import sys
sys.stdin=open("input.txt", "r")
def DFS(x, y):
    ch[x][y]=1
    if x==0:
        print(y)
    else:
        if y-1>=0 and board[x][y-1]==1 and ch[x][y-1]==0:
            DFS(x, y-1)
        elif y+1<10 and board[x][y+1]==1 and ch[x][y+1]==0:
            DFS(x, y+1)
        else:
            DFS(x-1, y)


board=[list(map(int, input().split())) for _ in range(10)]
ch=[[0]*10 for _ in range(10)]
for y in range(10):
    if board[9][y]==2:
        DFS(9, y)
'''