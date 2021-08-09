d = list(map(int, input().split()))
n = int(input())

for i in range(n):
    x, y = input().split()
    for j in range(1, 20):
        if d[j][int(y)] == 0:
            d[j][int(y)] = 1
        else:
            d[j][int(y)] = 0

    if d[int(x)][j] == 0:
        d[int(x)][j] = 1
    else:
        d[int(x)][j] = 0