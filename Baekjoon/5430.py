import sys
sys.stdin = open('input.txt')
from collections import deque


T = int(input())
for _ in range(T):
    p = input()
    n = int(input())
    x_list = input()

    arr = deque(x_list[1:len(x_list)-1].split(','))

    print(arr)

    P = []
    flag = 1
    cnt = 0
    for i in p:
        if i == 'R':
            flag *= -1
        else:

        #     if flag:
        #
        #     else:

    #         tmp = tmp[::-1]
    #     else:
    #         if tmp:
    #             tmp.pop(0)
    #         else:
    #             tmp = 'error'
    #             break

    # if tmp != 'error':
    #     print('[' + ','.join(map(str, tmp)) + ']')
    # else:
    #     print(tmp)