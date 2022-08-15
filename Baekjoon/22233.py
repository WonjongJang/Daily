import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


N, M = map(int, input().split())

D = {}
for _ in range(N):
    memo = input().rstrip()
    D[memo] = 1

for _ in range(M):
    tmp = list(input().rstrip().split(','))
    for t in tmp:
        if t in D:
            D.pop(t)

    print(len(D))
