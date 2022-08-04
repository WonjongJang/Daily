import sys
sys.stdin = open('input.txt')


N = int(input())
ins = {}
outs = []
for i in range(N):
    car = input()
    ins[car] = i

for o in range(N):
    car = input()
    outs.append(car)

ans = 0
for i in range(N-1):
    for j in range(i+1, N):
        if ins[outs[i]] > ins[outs[j]]:
            ans += 1
            break

print(ans)