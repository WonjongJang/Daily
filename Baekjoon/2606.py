import sys
sys.stdin = open('input.txt')

def virus(n):
    stack.append(n)
    visited[n] = 1

    for j in range(len(C)):
        if C[n][j] == 1 and visited[j] == 0:
            virus(j)

V = int(input())
E = int(input())

visited = [-1] + [0] * V
C = [[0] * (V+1) for _ in range(V+1)]

stack = []

for i in range(E):
    x, y = map(int, input().split())
    C[x][y] = 1
    C[y][x] = 1

virus(1)

print(len(stack)-1)