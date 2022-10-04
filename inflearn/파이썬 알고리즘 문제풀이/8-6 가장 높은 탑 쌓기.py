import sys
sys.stdin = open('8-6 input.txt')


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]

    data.sort(reverse=True)

    dp = [0]*N
    dp[0] = data[0][1]

    for i in range(1, N):
        max_h = 0
        for j in range(i-1, -1, -1):
            if data[i][2] < data[j][2]:
                max_h = max(max_h, dp[j])

        dp[i] = max_h + data[i][1]

    print(max(dp))



''' [풀이]
import sys
sys.stdin = open("input.txt", 'r')    
if __name__=="__main__":
    n=int(input())
    bricks=[]
    for i in range(n):
        a, b, c=map(int, input().split())
        bricks.append((a, b, c))
    bricks.sort(reverse=True)
    dy=[0]*n
    dy[0]=bricks[0][1]
    res=bricks[0][1];
    for i in range(1, n):
        max_h=0;
        for j in range(i-1, -1, -1):
            if bricks[j][2]>bricks[i][2] and dy[j]>max_h:
                max_h=dy[j]
        dy[i]=max_h+bricks[i][1]
        res=max(res, dy[i])
    print(res)
'''