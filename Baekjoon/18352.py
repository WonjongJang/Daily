import sys
import heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline
INF = sys.maxsize


N, M, K, X = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(M)]

dist = [INF for _ in range(N+1)]
v = [[] for _ in range(N+1)]
for d in data:
    v[d[0]].append(d[1])

que = []
heapq.heappush(que, [0, X])
dist[X] = 0

while que:
    d, cur = heapq.heappop(que)

    if dist[cur] < d:
        continue

    for i in v[cur]:
        nd = d + 1

        if dist[i] > nd:
            dist[i] = nd
            heapq.heappush(que, [nd, i])

flag = 0
for i in range(len(dist)):
    if dist[i] == K:
        print(i)
        if not flag:
            flag = 1
if not flag:
    print(-1)