import sys
sys.stdin = open('8-9 input.txt')


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))
    M = int(input())

    dp = [1000]*(M+1)
    dp[0] = 0
    for i in range(N):
        for j in range(data[i], M+1):
            dp[j] = min(dp[j], dp[j-data[i]]+1)

    print(dp[M])



''' [풀이]
import sys
sys.stdin = open("input.txt", 'r')    
if __name__=="__main__":
    n=int(input())
    coin=list(map(int, input().split()))
    m=int(input())
    dy=[1000]*(m+1);
    dy[0]=0
    for i in range(n):
        for j in range(coin[i], m+1):
            dy[j]=min(dy[j], dy[j-coin[i]]+1)
    print(dy[m])
'''