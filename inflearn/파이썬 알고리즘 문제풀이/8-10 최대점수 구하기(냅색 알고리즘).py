import sys
sys.stdin = open('8-10 input.txt')


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    dp = [0]*(M+1)
    for i in range(N):
        s, t = map(int, input().split())
        for j in range(M, t-1, -1):
            dp[j] = max(dp[j], dp[j-t]+s)

    print(dp[M])



''' [풀이]
import sys
sys.stdin = open("input.txt", 'r')    
if __name__=="__main__":
    n, m=map(int, input().split())
    dy=[0]*(m+1);
    for i in range(n):
        ps, pt=map(int, input().split())
        for j in range(m, pt-1, -1):
            dy[j]=max(dy[j], dy[j-pt]+ps)
    print(dy[m])
'''