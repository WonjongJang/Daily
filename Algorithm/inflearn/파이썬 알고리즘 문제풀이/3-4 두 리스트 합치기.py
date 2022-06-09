import sys
sys.stdin = open('3-4 input.txt', 'rt')


# 전체 반복 횟수
T = int(input())

# 전체 반복
for tc in range(1, T+1):
    N = int(input())
    arr_N = list(map(int, input().split()))
    M = int(input())
    arr_M = list(map(int, input().split()))

    ans = arr_N + arr_M
    ans.sort()

    print(*ans)



''' [풀이]
n=int(input())
a=list(map(int, input().split()))
m=int(input())
b=list(map(int, input().split()))
p1=p2=0
c=[]
while p1<n and p2<m:
    if a[p1]<b[p2]:
        c.append(a[p1])
        p1+=1
    else:
        c.append(b[p2])
        p2+=1
if p1<n:
    c=c+a[p1:]
if p2<m:
    c=c+b[p2:]
for x in c:
    print(x, end=' ')
'''