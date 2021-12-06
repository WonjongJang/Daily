import sys
sys.stdin = open('input.txt')


def adj_check(arr):
    q = []
    visited = [0] * (N+1)

    q.append(arr[0])
    visited[arr[0]] = 1
    cnt = 1
    sum = 0
    while q:
        x = q.pop(0)
        sum += population[x]
        for f in range(N+1):
            if adj[x][f] == 1 and f in arr and visited[f] == 0:
                cnt += 1
    if cnt == len(arr):
        return sum
    else:
        return 0

N = int(input())    # 구역의 개수
population = [0] + list(map(int, input().split()))    # 인구

adj = [[] for _ in range(N+1)]   # 인접 행렬
ans = 0
for n in range(1, N+1):
    data = list(map(int, input().split()))

    # for d in range(1, len(data)):
    #     adj[n][data[d]] = 1

print(adj)

area = list(range(1, N+1))
min_v = 100000

for i in range(1, (1<<len(area))):
    t_sum = 0
    temp1 = []
    temp2 = []
    for j in range(0, len(area)):
        if i & (1<<j):
            # print(r[j], end=' ')
            t_sum += population[area[j]]
            temp1.append(area[j])
        else:
            temp2.append(area[j])
    print()

    print('sum', t_sum)
    print(temp1)
    print(temp2)

    a1 = adj_check(temp1)

    if not a1:
        continue

    a2 = adj_check(temp2)

    if not a2:
        continue

    min_v = min(min_v, abs(a1-a2))

# 출력
print(min_v)