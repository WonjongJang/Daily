import sys
sys.stdin = open('8-7 input.txt')


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]

    dp = [[0]*N for _ in range(N)]
    dp[0][0] = data[0][0]
    for x in range(N):
        for y in range(N):
            if x == 0 and y == 0:
                continue
            if x == 0:
                dp[x][y] = dp[x][y-1] + data[x][y]
            elif y == 0:
                dp[x][y] = dp[x-1][y] + data[x][y]
            else:
                dp[x][y] = min(dp[x][y-1], dp[x-1][y]) + data[x][y]

    print(dp[N-1][N-1])



''' [풀이]
import sys
sys.stdin = open("input.txt", 'r')    
if __name__=="__main__":
    n=int(input())
    arr=[list(map(int, input().split())) for _ in range(n)]
    dy=[[0]*n for _ in range(n)]
    dy[0][0]=arr[0][0]
    for i in range(1, n):
        dy[0][i]=dy[0][i-1]+arr[0][i]
        dy[i][0]=dy[i-1][0]+arr[i][0]
    for i in range(1, n):
        for j in range(1, n):
            dy[i][j]=min(dy[i-1][j], dy[i][j-1])+arr[i][j]
    print(dy[n-1][n-1])
'''