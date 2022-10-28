import sys
sys.stdin = open('input.txt')


n, w, L = map(int, input().split())
A = list(map(int, input().split()))

bridge = [0] * w
T = 0

while True:
    bridge.pop(0)

    if A:
        if sum(bridge) + A[0] <= L:
            bridge.append(A.pop(0))
        else:
            bridge.append(0)

    T += 1

    if not bridge:
        break

print(T)