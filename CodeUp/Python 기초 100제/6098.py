g = []
for i in range(10):
    g.append(list(map(int, input().split())))

x = 1
y = 1

while True:
    if g[x][y] == 0:
        g[x][y] = 9
        y += 1
    elif g[x][y] == 2:
        g[x][y] = 9
        break
    elif g[x][y] == 1:
        x += 1
        y -= 1
        if g[x][y] == 0:
            g[x][y] = 9
            y += 1
        elif g[x][y] == 1:
            break
        elif g[x][y] == 2:
            g[x][y] = 9
            break

for j in g:
    for k in j:
        print(k, end=' ')
    print()