import sys
sys.stdin = open('3-7 input.txt', 'rt')


# 전체 반복 횟수
T = int(input())

# 전체 반복
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    s = e = N//2
    tot = 0
    for i in range(N):
        tmp = arr[i][s:e+1]
        tot += sum(tmp)

        if i < N//2:
            s -= 1
            e += 1
        else:
            s += 1
            e -= 1

    print(tot)



''' [풀이]
n=int(input())
a=[list(map(int, input().split())) for _ in range(n)]
res=0
s=e=n//2
for i in range(n):
    for j in range(s, e+1):
        res+=a[i][j]
    if i<n//2:
        s-=1
        e+=1
    else:
        s+=1
        e-=1
print(res)
'''