import sys
sys.stdin = open('input.txt')


def isVisited(a, b):
    if not visited[a][b]:
        visited[a][b] = 1   # 물의 양으로 저장하여 똑같은 양이 되었을 때 반복안하도록
        q.append((a, b))

def sol():
    q.append((0, 0))        # 처음에는 앞 두 물통 비어 있고, 세 번째 물통만 가득
    visited[0][0] = 1

    while q:
        a, b = q.pop(0)
        c = C - a - b       # C: 최초 가득 차있을 때 물의 양

        if not a:           # a가 비었을 때
            ans.append(c)   # ans에 저장

        # a -> b
        water = min(a, B-b)
        isVisited(a-water, b+water)

        # a -> c
        water = min(a, C-c)
        isVisited(a-water, b)

        # b -> a
        water = min(b, A-a)
        isVisited(a+water, b-water)

        # b -> c
        water = min(b, C-c)
        isVisited(a, b-water)

        # c -> a
        water = min(c, A-a)
        isVisited(a+water, b)

        # c -> b
        water = min(c, B-b)
        isVisited(a, b+water)

A, B, C = map(int, input().split())             # 각 물통의 부피

visited = [[0] * (B+1) for _ in range(A+1)]     # 방문

q = []      # queue
ans = []    # 첫 번째 물통이 비었을 때, 세 번째 물통에 담겨있는 물의 양 저장할 곳

sol()

ans.sort()
print(' '.join(map(str, ans)))