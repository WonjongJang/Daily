import sys
sys.stdin = open('input.txt')
from collections import deque


N = int(input())
cnt = 0
for _ in range(N):
    data = input()

    stack = deque()
    for i in range(len(data)):
        if not stack:
            stack.append(data[i])
        else:
            if stack[-1] == data[i]:
                stack.pop()
            else:
                stack.append(data[i])

    if not stack:
        # print(data)
        cnt += 1

print(cnt)
