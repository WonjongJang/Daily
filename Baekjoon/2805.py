import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


N, M = map(int, input().split())
trees = list(map(int, input().split()))

s = 1
e = 1000000000
while s <= e:
    m = (s+e)//2    # 절단기 설정 높이

    tot = 0
    for tree in trees:
        if tree-m > 0:
            tot += tree-m

    if tot < M:
        e = m-1
    else:
        s = m+1

print(e)