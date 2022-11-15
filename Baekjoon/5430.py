import sys
sys.stdin = open('input.txt')
from collections import deque


T = int(input())
for _ in range(T):
    p = input()
    n = int(input())
    x_list = input()

    if n:
        arr = deque(x_list[1:len(x_list)-1].split(','))
    else:
        arr = []

    flag = 1
    rev = 1
    for i in p:
        if i == 'R':
            rev *= -1
        else:
            if len(arr) < 1:
                flag = 0
                print('error')
                break
            else:
                if rev != -1:
                    arr.popleft()
                else:
                    arr.pop()

    if flag:
        if rev != 1:
            arr.reverse()
            print('[' + ','.join(map(str, arr)) + ']')
        else:
            print('[' + ','.join(map(str, arr)) + ']')