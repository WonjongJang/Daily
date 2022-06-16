import sys
sys.stdin = open('4-10 input.txt', 'rt')


# 전체 반복 횟수
T = int(input())

# 전체 반복
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    ans = [0] * N

    for i in range(N):
        for j in range(N):
            if arr[i] == 0 and ans[j] == 0:
                ans[j] = i+1
                break
            elif ans[j] == 0:
                arr[i] -= 1

    print(*ans)



''' [풀이]
n=int(input())
a=list(map(int, input().split()))
seq=[0]*n
for i in range(n):
    for j in range(n):
        if(a[i]==0 and seq[j]==0):
            seq[j]=i+1
            break
        elif seq[j]==0:
            a[i]-=1

for x in seq:
    print(x, end=' ')
'''