import sys
import heapq as hq
sys.stdin = open('5-10 input.txt', 'rt')


# 전체 반복 횟수
T = int(input())

# 전체 반복
for tc in range(1, T+1):
    arr = []
    while True:
        N = int(input())

        if N == -1:
            break

        if N == 0:
            if arr:
                print(hq.heappop(arr))
            else:
                print(-1)
        else:
            hq.heappush(arr, N)



''' [풀이]
import heapq as hq

a=[]
while True:
    n=int(input())
    if n==-1:
        break
    if n==0:
        if len(a)==0:
            print(-1)
        else:
            print(hq.heappop(a))
    else:
        hq.heappush(a, n)
'''