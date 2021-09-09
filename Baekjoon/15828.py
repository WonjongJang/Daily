import sys
sys.stdin = open('input.txt')

N = int(input())
router = []

while True:
    info = int(input())

    if info == -1:
        break

    if info == 0:
        router.pop(0)
    else:
        if len(router) < N:
            router.append(info)

if router:
    print(' '.join(map(str, router)))
else:
    print('empty')