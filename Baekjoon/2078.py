import sys
sys.stdin = open('input.txt')

A, B = map(int, input().split())

L = R = 0

while True:
    if A == 1 and B == 1:
        break

    if A > B:
        L += 1
        A = A - B
        B = B
    else:
        R += 1
        A = A
        B = B - A

print(L, R)


# sys.setrecursionlimit(10**9) -> 메모리 초과
#
# def tree(a, b, l, r):
#     global limit
#     # print(a, b, l, r)
#
#     if a > A or b > B:
#         return
#
#     if a == A and b == B:
#         limit = False
#         print(l, r)
#         return
#
#     if limit:
#         tree(a+b, b, l+1, r)
#     if limit:
#         tree(a, a+b, l, r+1)
#
#
# A, B = map(int, input().split())
#
# limit = True
#
# tree(1, 1, 0, 0)