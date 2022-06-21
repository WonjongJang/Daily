import sys
sys.stdin = open('4-5 input.txt', 'rt')


# 전체 반복 횟수
T = int(input())

# 전체 반복
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    arr.sort(key=lambda x: x[1])

    ans = []
    tmp = 0

    for s, e in arr:
        if s >= tmp:
            ans.append((s, e))
            tmp = e

    print(len(ans))




''' [풀이]
n=int(input())
meeting=[]
for i in range(n):
    a, b=map(int, input().split())
    meeting.append((a, b))
meeting.sort(key=lambda x : (x[1], x[0]))
et=0
cnt=0
for x, y in meeting:
    if x>=et:
        et=y
        cnt+=1
print(cnt)
'''