n = int(input())
a = list(map(int, input().split()))

count_list = []
for i in range(24):
    count_list.append(0)

for j in range(n):
    count_list[a[j]] += 1

for k in range(1, 24):
    print(count_list[k], end=' ')