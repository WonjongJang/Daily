import sys
sys.stdin = open('3-9 input.txt', 'rt')


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 전체 반복 횟수
T = int(input())

# 전체 반복
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0
    for x in range(N):
        for y in range(N):
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if 0 <= nx < N and 0 <= ny < N:
                    if arr[nx][ny] >= arr[x][y]:
                        break
            else:
                cnt += 1

    print(cnt)



''' [풀이]
dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]
n=int(input())
a=[list(map(int, input().split())) for _ in range(n)]
a.insert(0, [0]*n)
a.append([0]*n)
for x in a:
    x.insert(0, 0)
    x.append(0)

cnt=0
for i in range(1, n+1):
    for j in range(1, n+1):
        if all(a[i][j]>a[i+dx[k]][j+dy[k]] for k in range(4)):
            cnt+=1
print(cnt)
'''