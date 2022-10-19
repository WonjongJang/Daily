import sys
sys.stdin = open('input.txt')


N = int(input())
adj = [[0]*(N+1) for _ in range(N+1)]
P = [0]*(N+1)
for i in range(1, N+1):
    t, p = map(int, input().split())

    if i+t <= N:
        adj[i][i+t] = 1
    P[i] = p

print(adj)
print(P)

# def recur(L, sum):
#     global max_v
#     print(L, sum)
#     if L+data[L][0] > N:
#         max_v = max(max_v, sum)
#     else:
#         recur(L+data[L][0], sum+data[L][1])
#
# N = int(input())
# data = [[0, 0]]
# for _ in range(N):
#     t, p = map(int, input().split())
#     data.append([t, p])
#
# print(data)
# max_v = 0
# for i in range(1, N+1):
#     t = data[i][0]
#     p = data[i][1]
#     if i+t <= N:
#         recur(i, p)
#
# print(max_v)