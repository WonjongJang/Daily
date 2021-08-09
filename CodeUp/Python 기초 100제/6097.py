h, w = map(int, input().split())
n = int(input())

list = []
for h_i in range(h):
    list.append([])
    for w_i in range(w):
        list[h_i].append(0)

for n_i in range(n):
    l, d, x, y = map(int, input().split())
    if d == 0:
        for i in range(l):
            list[x-1][y-1] = 1
            y += 1
    else:
        for i in range(l):
            list[x-1][y-1] = 1
            x += 1

for li in list:
    for l in li:
        print(l, end=' ')
    print()