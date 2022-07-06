import sys
sys.stdin = open('6-1 input.txt', 'rt')


def recur(x):
    if x == 0:
        return
    else:
        recur(x//2)
        print(x%2, end='')

# 전체 반복 횟수
T = int(input())

# 전체 반복
for tc in range(1, T+1):
    N = int(input())

    recur(N)
    print('')



''' [풀이]
def DFS(x):
    if x==0:
        return
    else:
        DFS(x//2)
        print(x%2, end='')

n=int(input())
DFS(n)
'''