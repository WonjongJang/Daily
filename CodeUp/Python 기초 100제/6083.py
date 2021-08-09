r, g, b = input().split()

r = int(r)
g = int(g)
b = int(b)

sum = 0

for i in range(r):
    for j in range(g):
        for k in range(b):
            print(i, j, k)
            sum += 1
print(sum)