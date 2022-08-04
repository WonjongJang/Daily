import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


N = int(input())
S = set()
for _ in range(N):
    n, s = map(str, input().split())
    if s == 'enter':
        S.add(n)
    else:
        S.remove(n)

new_S = sorted(S, reverse=True)

for s in new_S:
    print(s)