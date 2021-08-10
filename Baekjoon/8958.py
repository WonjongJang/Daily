import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    ox = input()
    t = 0
    p = 0
    for i in range(len(ox)):
        if ox[i] == 'O':
            t = t + 1 + p
            p += 1
        else:
            p = 0
    print(t)
