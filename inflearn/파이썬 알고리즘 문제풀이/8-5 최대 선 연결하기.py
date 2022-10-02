import sys
sys.stdin = open('8-5 input.txt')


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))

    dp = [0]*N
    dp[0] = 1

    for i in range(1, N):
        max_v = 0
        for j in range(i-1, -1, -1):
            if data[i] > data[j]:
                max_v = max(max_v, dp[j])

        dp[i] = max_v+1

    print(max(dp))



''' [풀이]
import sys
sys.stdin = open("input.txt", 'r')
n=int(input())
arr=list(map(int, input().split()))
arr.insert(0,0)
dy=[0]*(n+1)
dy[1]=1
res=0
for i in range(2, n+1):
    max=0
    for j in range(i-1, 0, -1):
        if arr[j]<arr[i] and dy[j]>max:
            max=dy[j]
    dy[i]=max+1
    if dy[i]>res:
        res=dy[i]
print(res)
'''