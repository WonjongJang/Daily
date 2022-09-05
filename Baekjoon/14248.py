import sys
sys.stdin = open('input.txt')


def recur(L):
    v[L] = 1

    l = L - data[L]
    r = L + data[L]
    if 0 <= l < N and not v[l]:
        recur(l)
    if 0 <= r < N and not v[r]:
        recur(r)


N = int(input())
data = list(map(int, input().split()))
S = int(input())

v = [0]*N
recur(S-1)

print(v.count(1))