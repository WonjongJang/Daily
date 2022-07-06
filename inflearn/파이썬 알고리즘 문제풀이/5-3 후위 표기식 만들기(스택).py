import sys
sys.stdin = open('5-3 input.txt', 'rt')


# 전체 반복 횟수
T = int(input())

# 전체 반복
for tc in range(1, T+1):
    arr = input()

    ans = ''
    stack = []
    for a in arr:
        if a.isdecimal():
            ans += a
        else:
            if a == '(':
                stack.append(a)
            elif a in '+-':
                while stack and stack[-1] != '(':
                    ans += stack.pop()
                stack.append(a)
            elif a in '*/':
                while stack and stack[-1] in '*/':
                    ans += stack.pop()
                stack.append(a)
            elif a == ')':
                while stack and stack[-1] != '(':
                    ans += stack.pop()
                stack.pop()

    while stack:
        ans += stack.pop()

    print(ans)



''' [풀이]
a=input()
stack=[]
res=''
for x in a:
    if x.isdecimal():
        res+=x
    else:
        if x=='(':
            stack.append(x)
        elif x=='*' or x=='/':
            while stack and (stack[-1]=='*' or stack[-1]=='/'):
                res+=stack.pop()
            stack.append(x)
        elif x=='+' or x=='-':
            while stack and stack[-1]!='(':
                res+=stack.pop()
            stack.append(x)
        elif x==')':
            while stack and stack[-1]!='(':
                res+=stack.pop()
            stack.pop()
while stack:
    res+=stack.pop()
print(res)
'''