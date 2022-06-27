import sys
sys.stdin = open('6-4 input.txt', 'rt')


def recur(x):
    global ans

    if ans == "YES":
        return

    if x == N:
        s1 = 0
        s2 = 0
        for i in range(N):
            if V[i]:
                s1 += arr[i]
                # print(i, end=' ')
            else:
                s2 += arr[i]
        if s1 == s2:
            ans = "YES"
            return
    else:
        V[x] = 1
        recur(x+1)
        V[x] = 0
        recur(x+1)

# 전체 반복 횟수
T = int(input())

# 전체 반복
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    ans = "NO"
    V = [0] * N

    recur(0)

    print(ans)



''' [풀이]
def DFS(L, sum):
    if sum>total//2:
        return
    if L==n:
        if sum==(total-sum):
            print("YES")
            sys.exit(0)
    else:
        DFS(L+1, sum+a[L])
        DFS(L+1, sum)

n=int(input())
a=list(map(int, input().split()))
total=sum(a)
DFS(0, 0)
print("NO")
'''