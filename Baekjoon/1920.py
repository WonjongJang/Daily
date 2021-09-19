import sys
sys.stdin = open('input.txt')

N = int(input())
A = list(map(int, input().split()))
M = int(input())
X = list(map(int, input().split()))

A.sort()

for m in range(M):
    start = 0
    end = N-1
    check = False

    while start <= end:
        mid = (start + end) // 2

        if X[m] == A[mid]:
            check = True
            break
        elif X[m] < A[mid]:
            end = mid - 1
        elif X[m] > A[mid]:
            start = mid + 1

    if check:
        print(1)
    else:
        print(0)
