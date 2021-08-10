n = int(input())
l = list(map(int, input().split()))

min = max = l[0]

for i in range(1, n):
    if min > l[i]:
        min = l[i]
    if max < l[i]:
        max = l[i]
print(min, max)