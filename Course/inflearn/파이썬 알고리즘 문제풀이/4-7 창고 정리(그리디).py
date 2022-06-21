import sys
sys.stdin = open('4-7 input.txt', 'rt')


# 전체 반복 횟수
T = int(input())

# 전체 반복
for tc in range(1, T+1):
    L = int(input())
    arr = list(map(int, input().split()))
    M = int(input())

    cnt = 0

    while cnt < M:
        cnt += 1

        max_idx = arr.index(max(arr))
        min_idx = arr.index(min(arr))

        arr[max_idx] -= 1
        arr[min_idx] += 1

    arr.sort(reverse=True)

    print(arr[0]-arr[-1])



''' [풀이]
L=int(input())
a=list(map(int, input().split()))
m=int(input())
a.sort()
for _ in range(m):
    a[0]+=1
    a[L-1]-=1
    a.sort()

print(a[L-1]-a[0])
'''