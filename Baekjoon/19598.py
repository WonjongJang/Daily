import sys
import heapq
sys.stdin = open('input.txt')


N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]

data.sort()

meeting = [data[0][1]]
for i in range(1, N):
    if meeting[0] > data[i][0]:
        heapq.heappush(meeting, data[i][1])
    else:
        heapq.heapreplace(meeting, data[i][1])

print(len(meeting))