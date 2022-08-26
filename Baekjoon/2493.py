import sys
sys.stdin = open('input.txt')


N = int(input())
data = list(map(int, input().split()))

ans = [0] * N
stack = []
for i in range(N):
    while stack:
        if stack[-1][0] < data[i]:
            stack.pop()
        else:
            ans[i] = stack[-1][1]+1
            break

    stack.append((data[i], i))

print(*ans)



''' 시간초과
N = int(input())
data = list(map(int, input().split()))

for i in range(N):
    if not i:
        print(0, end=' ')
        continue
    for j in range(i-1, -1, -1):
        if data[j] > data[i]:
            print(j+1, end=' ')
            break
    else:
        print(0, end=' ')
'''