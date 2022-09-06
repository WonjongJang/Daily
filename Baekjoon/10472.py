import sys
sys.stdin = open('input.txt')


dx = []

def recur(x, y):
    pass

T = int(input())
for tc in range(1, T+1):
    data = [list(input()) for _ in range(3)]

    print(data)
    for x in range(3):
        for y in range(3):
            recur(x, y)