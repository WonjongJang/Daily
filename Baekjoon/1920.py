import sys
sys.stdin = open('input.txt')


N = int(input())
A = list(map(int, input().split()))
M = int(input())
X = list(map(int, input().split()))

A.sort()

for x in X:
    l = 0
    r = N-1
    check = 0
    while l <= r:
        mid = (l+r)//2

        if x == A[mid]:
            check = 1
            break
        elif x > A[mid]:
            l = mid + 1
        else:
            r = mid - 1

    print(check)



'''
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
'''