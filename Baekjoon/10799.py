import sys
sys.stdin = open('input.txt')


data = input()

stack = []
cnt = 0
for i in range(len(data)):
    if data[i] == '(':
        stack.append(data[i])
    else:
        if data[i-1] == '(':
            stack.pop()
            cnt += len(stack)
        else:
            stack.pop()
            cnt += 1

print(cnt)
