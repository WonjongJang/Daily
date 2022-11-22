import sys
sys.stdin = open('input.txt')


def recur(c):
    if c == M:
        print(*ans)
    else:
        for i in range(N):
            if v[i] == 0:
                if c > 0 and ans[c-1] > arr[i]:
                    continue
                else:
                    ans[c] = arr[i]
                    v[i] = 1
                    recur(c+1)
                    v[i] = 0

N, M = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

ans = [0]*M
v = [0]*N

recur(0)