import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10 ** 6)


def check_ladder(x):
    for i in range(len(ladder)):
        if x == ladder[i][0]:
            return ladder[i][1]
    return 0

def check_snake(x):
    for i in range(len(snake)):
        if x == snake[i][0]:
            return snake[i][1]
    return 0

def sol(x, cnt):
    print(x, cnt)
    if x >= 100:
        return

    for i in range(1, 7):
        if check_ladder(x+i):
            sol(check_ladder(x+i), cnt+1)
        elif check_snake(x+i):
            continue
        else:
            sol(x+i, cnt+1)

N, M = map(int, input().split())    # N: 사다리 수, M: 뱀 수
ladder = [list(map(int, input().split())) for _ in range(N)]
snake = [list(map(int, input().split())) for _ in range(M)]

max_
for i in range(len(ladder)):


print(ladder)
print(snake)

# sol(1, 0)

# ladder.sort()
#
# print(ladder)

