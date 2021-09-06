import sys
sys.stdin = open('input.txt')

N = int(input())
C = list(range(1, N+1))
stack = []
ans = []

for n in range(N):
    number = int(input())

    if stack and stack[-1] != number and number not in C:
        ans.append('NO')
        break

    if stack == []:
        while True:
            if C[0] == number:
                stack.append(C.pop(0))
                ans.append('+')
                break

            stack.append(C.pop(0))
            ans.append('+')
    elif stack and stack[-1] != number:
        if C:
            while True:
                if C[0] == number:
                    stack.append(C.pop(0))
                    ans.append('+')
                    break

                stack.append(C.pop(0))
                ans.append('+')
        else:
            ans.append('NO')
            break

    if stack and stack[-1] == number:
        stack.pop()
        ans.append('-')

if 'NO' in ans:
    print('NO')
else:
    for p in range(len(ans)):
        print(ans[p])