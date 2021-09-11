import sys
from collections import deque
sys.stdin = open('input.txt')

N = int(input())

q = deque()

for n in range(N):
    order = sys.stdin.readline().split()
    # print(order)
    if order[0] == 'push':
        q.append(order[1])
    elif q and order[0] == 'pop':
        print(q.popleft())
    elif order[0] == 'size':
        print(len(q))
    elif order[0] == 'empty':
        if q:
            print(0)
        else:
            print(1)
    elif q and order[0] == 'front':
        print(q[0])
    elif q and order[0] == 'back':
        print(q[-1])
    else:
        print(-1)