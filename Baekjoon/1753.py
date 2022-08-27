import sys
sys.stdin = open('input.txt')
import heapq
INF = sys.maxsize
input = sys.stdin.readline


V, E = map(int, input().split())
K = int(input())
data = [list(map(int, input().split())) for _ in range(E)]

dist = [INF for i in range(V+1)]
v = [[] for _ in range(V+1)]
for i in data:
    v[i[0]].append((i[1], i[2]))

que = []
heapq.heappush(que, [0, K])
dist[K] = 0

while que:
    d, cur = heapq.heappop(que)

    if d > dist[cur]:
        continue

    for i in v[cur]:
        nd = d + i[1]

        if dist[i[0]] > nd:
            dist[i[0]] = nd
            heapq.heappush(que, [nd, i[0]])

for i in dist[1:]:
    if i == INF:
        print('INF')
        continue
    print(i)