import sys
sys.stdin = open('input.txt')

def dfs(v):
    global N

    visited_d[v] = 1
    print(v, end=' ')

    for d in range(N+1):
        if C[v][d] == 1 and visited_d[d] == 0:
            dfs(d)

def bfs(v):
    global N
    queue = []

    queue.append(v)
    visited_b[v] = 1

    while queue:
        t = queue.pop(0)
        print(t, end=' ')
        for b in range(N+1):
            if C[t][b] == 1 and visited_b[b] == 0:
                queue.append(b)
                visited_b[b] = 1

N, M, V = map(int, input().split())

C = [[0] * (N+1) for _ in range(N+1)]
visited_d = [0] * (N+1)
visited_b = [0] * (N+1)

for m in range(M):
    x, y = map(int, input().split())
    C[x][y] = 1
    C[y][x] = 1

dfs(V)
print()
bfs(V)