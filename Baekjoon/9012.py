import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(T):
    stack = []
    ps = input()
    if ps[0] == ')':    # )로 시작하는 경우
        print('NO')
        continue
    for i in range(len(ps)):
        if ps[i] == '(':
            stack.append(ps[i])
        else:
            if stack:
                stack.pop()
            else:
                stack.append(ps[i])
                break
    if stack:
        print('NO')
    else:
        print('YES')