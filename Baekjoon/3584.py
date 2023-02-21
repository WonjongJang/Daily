import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10**9)


# 루트 노드부터 각 노드까지의 깊이 계산
def recur(x, depth):
    # v[x] = True
    d[x] = depth
    for x_child in graph[x]:
        # if not v[x_child]:
            recur(x_child, depth+1)

def lca(a, b):
    # 깊이 맞추기
    while d[a] != d[b]:
        if d[a] > d[b]:
            a = parent[a]
        else:
            b = parent[b]

    # 노드 맞추기
    while a != b:
        a = parent[a]
        b = parent[b]

    return a

T = int(input())
for _ in range(T):
    N = int(input())

    parent = [0] * (N+1)    # 부모 노드 정보
    graph = [[] for _ in range(N+1)]    # 그래프 정보
    d = [0] * (N+1) # 각 노드까지의 깊이
    # v = [0] * (N+1) # 각 노드의 깊이가 계산되었는지 여부 (트리는 임의의 두 정점 사이의 경로가 유일하여 path가 겹치지 않음)

    for _ in range(N-1):
        a, b = map(int, input().split())
        graph[a].append(b)
        parent[b] = a

    # 루트 노드 찾아서 각 노드의 깊이를 구함
    for i in range(1, N+1):
        if parent[i] == 0:
            recur(i, 0)
            break

    x, y = map(int, input().split())
    print(lca(x, y))