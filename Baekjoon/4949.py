import sys
sys.stdin = open('input.txt')


while True:
    stack = []
    string = input()

    if string == '.':
        break

    for i in range(len(string)):
        if string[i] == '.':
            break
        if string[i] in '([':
            stack.append(string[i])
        elif string[i] == ')':
            if stack:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    break
            else:
                stack.append(string[i])
                break
        elif string[i] == ']':
            if stack:
                if stack[-1] == '[':
                    stack.pop()
                else:
                    break
            else:
                stack.append(string[i])
                break

    if stack:
        print('no')
    else:
        print('yes')