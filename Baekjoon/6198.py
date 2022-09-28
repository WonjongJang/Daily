import sys
sys.stdin = open('input.txt')


N = int(input())
data = list(int(input()) for _ in range(N))

ans = 0
stack = []
for i in range(N):
    while stack:
        if stack[-1] <= data[i]:
            stack.pop()
        else:
            ans += len(stack)
            break

    stack.append(data[i])

print(ans)



''' [시간 초과]
N = int(input())
data = list(int(input()) for _ in range(N))

ans = 0
for i in range(N):
    for j in range(i+1, N):
        if data[i] <= data[j]:
            break
        ans += 1

print(ans)
'''