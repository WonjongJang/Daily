import sys
sys.stdin = open('3-8 input.txt', 'rt')


# 전체 반복 횟수
T = int(input())

# 전체 반복
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    M = int(input())
    for m in range(M):
        r, lr, d = map(int, input().split())
        nr = r-1
        nd = d%N

        if lr:
            arr[nr] = arr[nr][N-nd:] + arr[nr][:N-nd]
        else:
            arr[nr] = arr[nr][nd:] + arr[nr][:nd]

    s = 0
    e = N
    tot = 0
    for i in range(N):
        tmp = arr[i][s:e]
        tot += sum(tmp)

        if i < N//2:
            s += 1
            e -= 1
        else:
            s -= 1
            e += 1

    print(tot)



''' [풀이]
n=int(input())
a=[list(map(int, input().split())) for _ in range(n)]
m=int(input())
for i in range(m):
    h, t, k=map(int, input().split())
    if(t==0):
        for _ in range(k):
            a[h-1].append(a[h-1].pop(0))
    else:
        for _ in range(k):
            a[h-1].insert(0, a[h-1].pop())

res=0
s=0
e=n-1
for i in range(n):
    for j in range(s, e+1):
        res+=a[i][j]
    if i<n//2:
        s+=1
        e-=1
    else:
        s-=1
        e+=1
print(res)
'''