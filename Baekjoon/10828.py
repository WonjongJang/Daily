import sys
sys.stdin = open('input.txt')

N = int(input())

stack = []

for n in range(N):
    order = sys.stdin.readline().split()
    if order[0] == 'push':
        stack.append(int(order[1]))
    elif order[0] == 'pop' and stack:
        print(stack.pop())
    elif order[0] == 'size':
        print(len(stack))
    elif order[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif order[0] == 'top' and stack:
        print(stack[-1])
    else:
        print(-1)