import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


N, P = map(int, input().split())
stack = [[] for _ in range(7)]

cnt = 0
for _ in range(N):
    l, p = map(int, input().split())
    if stack[l]:
        if stack[l][-1] < p:
            stack[l].append(p)
            cnt += 1
        elif stack[l][-1] > p:
            while stack[l] and stack[l][-1] > p:
                stack[l].pop()
                cnt += 1
            if stack[l] and stack[l][-1] == p:
                continue
            stack[l].append(p)
            cnt += 1
        else:
            continue
    else:
        stack[l].append(p)
        cnt += 1

print(cnt)



''' [시간초과 & 틀림]
N, P = map(int, input().split())
stack = [[] for _ in range(7)]

cnt = 0
for _ in range(N):
    l, p = map(int, input().split())
    if stack[l]:
        if p in stack[l]:
            while True:
                if stack[l][-1] == p:
                    break
                stack[l].pop()
                cnt += 1
        else:
            if stack[l][-1] < p:
                stack[l].append(p)
                cnt += 1
            elif stack[l][-1] > p:
                while stack[l]:
                    if stack[l][-1] < p:
                        break
                    stack[l].pop()
                    cnt += 1
                stack[l].append(p)
                cnt += 1
    else:
        stack[l].append(p)
        cnt += 1

print(cnt)
'''