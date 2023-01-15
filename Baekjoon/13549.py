import sys
sys.stdin = open('input.txt')
from collections import deque


move = [2, 1, -1]

N, K = map(int, input().split())

if N >= K:  # N이 K보다 크면 -1로만 갈 수 있음
    print(N-K)  # 떨어진 칸 수 만큼 이동
    sys.exit()  # 종료

v = [-1]*100001
que = deque()
que.append(N)   # 수빈 위치
v[N] = 0
while que:  # bfs
    x = que.popleft()

    if x == K:  # 동생 위치에 도착
        print(v[x])
        break

    for m in move:
        if m != 2:  # 걸음
            nx = x + m
        else:       # 순간이동
            nx = x * m

        if 0 <= nx <= 100000:
            # 먼저 방문한 곳이 최단 시간이 아닐 수 있음
            if m != 2 and (v[nx] == -1 or v[nx] > v[x]+1):  # 걸음
                v[nx] = v[x]+1
                que.append(nx)
            elif m == 2 and (v[nx] == -1 or v[nx] > v[x]):  # 순간이동
                v[nx] = v[x]
                que.append(nx)