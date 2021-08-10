n, x = input().split()
a = list(map(int, input().split()))

n = int(n)
x = int(x)

for i in range(n):
    if a[i] < x:
        print(a[i], end=' ')