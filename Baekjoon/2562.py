l = []

for i in range(9):
    l.append(int(input()))

max = l[0]
max_idx = 0

for j in range(1, 9):
    if max < l[j]:
        max = l[j]
        max_idx = j + 1
if max == l[0]:
    max_idx = 1

print(max)
print(max_idx)