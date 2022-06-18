import sys
sys.stdin = open('5-4 input.txt', 'rt')


# 전체 반복 횟수
T = int(input())

# 전체 반복
for tc in range(1, T+1):
    arr = input()

    ans = 0
    stack = []
    for a in arr:
        if a.isdecimal():
            stack.append(int(a))
        else:
            if a == '+':
                y = stack.pop()
                x = stack.pop()
                stack.append(x+y)
            elif a == '-':
                y = stack.pop()
                x = stack.pop()
                stack.append(x-y)
            elif a == '*':
                y = stack.pop()
                x = stack.pop()
                stack.append(x*y)
            else:
                y = stack.pop()
                x = stack.pop()
                stack.append(x/y)

    print(*stack)



''' [풀이]
a=input()
stack=[]
for x in a:
    if x.isdecimal():
        stack.append(int(x))
    else:
        if x=='+':
            n1=stack.pop()
            n2=stack.pop()
            stack.append(n2+n1)
        elif x=='-':
            n1=stack.pop()
            n2=stack.pop()
            stack.append(n2-n1)
        elif x=='*':
            n1=stack.pop()
            n2=stack.pop()
            stack.append(n2*n1)
        elif x=='/':
            n1=stack.pop()
            n2=stack.pop()
            stack.append(n2/n1)
print(stack[0])
'''