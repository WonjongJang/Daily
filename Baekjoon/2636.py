import sys
sys.stdin = open('input.txt')
from collections import deque


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs():
    que = deque()
    que.append((0, 0))
    v[0][0] = 1
    cnt = 0

    while que:
        x, y = que.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < X and 0 <= ny < Y and not v[nx][ny]:
                if not data[nx][ny]:
                    que.append((nx, ny))
                    v[nx][ny] = 1
                else:
                    data[nx][ny] = 0
                    v[nx][ny] = 1
                    cnt += 1

    return cnt

X, Y = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(X)]

ans = []
time = 0
while True:
    v = [[0]*Y for _ in range(X)]

    cnt = bfs()
    ans.append(cnt)

    if not cnt:
        break

    time += 1

print(time)
print(ans[-2])





