import sys
sys.stdin = open('input.txt')
from collections import deque


dx = [-1, 0, 1, 0, -1, -1, 1, 1, 0]
dy = [0, 1, 0, -1, -1, 1, -1, 1, 0]

def bfs(x, y):
    q = deque()
    q.append((x, y))

    while q:
        for _ in range(len(q)):
            x, y = q.popleft()

            if data[x][y] == '#':
                continue

            if x == 0 and y == 7:
                return 1

            for d in range(9):
                nx = x + dx[d]
                ny = y + dy[d]
                if 0 <= nx < 8 and 0 <= ny < 8 and data[nx][ny] == '.':
                    q.append((nx, ny))

        data.pop()
        data.appendleft(['.', '.', '.', '.', '.', '.', '.', '.'])

    return 0


data = deque(list(input()) for _ in range(8))

print(bfs(7, 0))

