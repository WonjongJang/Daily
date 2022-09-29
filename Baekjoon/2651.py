import sys
sys.stdin = open('input.txt')

#
# def recur(L, sum):
#     if L == C:
#         print(v)
#     else:
#         v[L+1] = 1
#         recur(L+1, 0)
#         v[L+1] = 0
#         recur(L+1, sum+D[L])


Max = int(input())
C = int(input())
D = list(map(int, input().split()))
T = list(map(int, input().split()))

# v = [0]*(C+1)
# recur(0, 0)

dp = [0]*(C+2)
print(dp)
