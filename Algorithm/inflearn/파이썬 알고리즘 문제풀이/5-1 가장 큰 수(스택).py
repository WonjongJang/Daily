import sys
sys.stdin = open('5-1 input.txt', 'rt')


# 전체 반복 횟수
T = int(input())

# 전체 반복
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, str(N)))

    stack = []

    for a in arr:
        while stack and M > 0 and a > stack[-1]:
            stack.pop()
            M -= 1
        stack.append(a)
    if M:
        stack = stack[:-M]

    print(''.join(map(str, stack)))



''' [풀이]
num, m=map(int, input().split())
num=list(map(int, str(num)))
stack=[]
for x in num:
    while stack and m>0 and stack[-1]<x:
        stack.pop()
        m-=1
    stack.append(x)
if m!=0:
    stack=stack[:-m]
res=''.join(map(str, stack))
print(res)
'''