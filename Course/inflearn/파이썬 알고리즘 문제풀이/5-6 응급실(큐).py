import sys
sys.stdin = open('5-6 input.txt', 'rt')


# 전체 반복 횟수
T = int(input())

# 전체 반복
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    queue = []
    for i, v in enumerate(arr):
        queue.append([v, i])

    cnt = 0
    while True:
        tmp = queue.pop(0)

        if tmp[0] < max(queue)[0]:
            queue.append(tmp)
        else:
            cnt += 1
            if tmp[1] == M:
                break

    print(cnt)



''' [풀이]
n, m=map(int, input().split())
Q=[(pos, val) for pos, val in enumerate(list(map(int, input().split())))]
Q=deque(Q)
cnt=0
while True:
    cur=Q.popleft()
    if any(cur[1]<x[1] for x in Q):
        Q.append(cur)
    else:
        cnt+=1
        if cur[0]==m:
            print(cnt)
            break
'''