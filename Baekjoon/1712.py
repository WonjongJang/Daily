A, B, C = map(int, input().split())

if B < C:
    ans = A // (C - B) + 1
else:
    ans = -1

print(ans)