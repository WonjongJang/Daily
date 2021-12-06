import sys
sys.stdin = open('input.txt')

N = int(input())    # 학생 수
exp = []            # 예상 등수
for _ in range(N):
    exp.append(int(input()))

exp.sort()  # 예상 등수를 오름차순 정렬해야 실제 등수가 1부터 오름차순인 것과 차이가 가장 적을 것

rank = list(range(1, N+1))  # 실제 등수

sum = 0
for i in range(N):
    sum += abs(exp[i] - rank[i])    # 예상 - 실제 -> 절대값

# 출력
print(sum)



# 시간 초과 (모든 순열을 구해서 최소값 도출)
# import sys
# sys.stdin = open('input.txt')
# sys.setrecursionlimit(10**9)
#
# def perm(n, k):
#     global min_v
#
#     if k == n:
#         # print(real)
#         sum = 0
#         for i in range(n):
#             sum += abs(exp[i] - real[i])
#         # print(sum)
#         min_v = min(min_v, sum)
#     else:
#         for p in range(n):
#             if used[p] == 0:
#                 used[p] = 1
#                 real[k] = rank[p]
#                 print(real)
#                 perm(n, k+1)
#                 used[p] = 0
#
# N = int(input())    # 학생 수
# exp = []
# for _ in range(N):
#     exp.append(int(input()))
#
# min_v = 100000
# rank = list(range(1, N+1))
# real = [0] * N
# used = [0] * N
#
# perm(N, 0)
#
# # 출력
# print(min_v)