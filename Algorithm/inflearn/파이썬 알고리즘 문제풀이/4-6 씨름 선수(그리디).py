import sys
sys.stdin = open('4-6 input.txt', 'rt')


# 전체 반복 횟수
T = int(input())

# 전체 반복
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    arr.sort(reverse=True)

    ans = []
    tmp = arr[0][1]
    for t, w in arr:
        if w >= tmp:
            ans.append((t, w))
            tmp = w

    print(len(ans))



''' [풀이]
n=int(input())
body=[]
for i in range(n):
    a, b=map(int, input().split())
    body.append((a, b))
body.sort(reverse=True)
largest=0
cnt=0
for x, y in body:
    if y>largest:
        largest=y
        cnt+=1
print(cnt)
'''