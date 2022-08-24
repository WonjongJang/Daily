import sys
sys.stdin = open('7-7 input.txt')
from collections import deque


T = int(input())
for tc in range(1, T+1):
    S, E = map(int, input().split())

    v = [0] * 10001

    if S < E:
        jump = [1, -1, 5]
        q = deque()
        q.append((S, 0))
        v[S] = 1
        while q:
            loca, cnt = q.popleft()

            if loca == E:
                print(cnt)
                break

            for j in range(3):
                n_loca = loca + jump[j]
                if 1 <= n_loca <= 10000 and not v[n_loca]:
                    q.append((n_loca, cnt+1))
                    v[n_loca] = 1
    else:
        print(S-E)



''' [풀이]
import sys
from collections import deque
sys.stdin=open("input.txt", "r")
MAX = 10000
ch = [0] * (MAX+1)
dis = [0] * (MAX+1)
n,m = map(int,input().split())
ch[n] = 1
dis[n] = 0
dQ = deque()
dQ.append(n)
while dQ:
    now = dQ.popleft()
    if now==m:
        break
    for next in (now-1, now+1, now+5):
        if 1 <= next <= MAX:
            if ch[next]==0:
                dQ.append(next)
                ch[next] = 1
                dis[next] = dis[now]+1
                
print(dis[m])
'''