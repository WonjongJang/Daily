import sys
sys.stdin = open('input.txt')


N = int(input())
number = [list(range(1, 10))]

print(number)
for n in number:






# 시간 초과
# def recur(s, idx):
#     global ans
#
#     if idx == N-1:
#         # print(number)
#         ans += 1
#         return
#
#     ms = s-1
#     ps = s+1
#     n_idx = idx+1
#     if 0 <= ms <= 9:
#         number[n_idx] = ms
#         recur(ms, n_idx)
#         number[n_idx] = 0
#     if 0 <= ps <= 9:
#         number[n_idx] = ps
#         recur(ps, n_idx)
#         number[n_idx] = 0
#
# N = int(input())
# number = [0]*N
#
# ans = 0
# for start in range(1, 10):
#     number[0] = start
#     recur(start, 0)
#     number[0] = 0
#
# print(ans % 1000000000)