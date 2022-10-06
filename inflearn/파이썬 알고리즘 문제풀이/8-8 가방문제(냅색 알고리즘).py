import sys
sys.stdin = open('8-8 input.txt')


T = int(input())
for tc in range(1, T+1):
    N, W = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]

    dp = [0]*(W+1)

    for i in range(N):
        w = data[i][0]
        v = data[i][1]
        for j in range(w, W+1):
            dp[j] = max(dp[j], dp[j-w]+v)

    print(dp[W])



''' [풀이]
import sys
sys.stdin = open("input.txt", 'r')    
if __name__=="__main__":
    n, m=map(int, input().split())
    dy=[0]*(m+1);
    for i in range(n):
        w, v=map(int, input().split())
        for j in range(w, m+1):
            dy[j]=max(dy[j], dy[j-w]+v)
    print(dy[m])
'''