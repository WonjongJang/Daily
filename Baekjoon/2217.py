k = int(input())

k_w = []
for _ in range(k):
    k_w.append(int(input()))

k_w.sort(reverse=True)
# for i in range(k-1):
#     max = 0
#     for j in range(i+1, k):
#         if k_w[max] < k_w[j]:
#             max = j
#     k_w[i], k_w[j] = k_w[j], k_w[i]

n_k_w = []
for ki in range(1, k+1):
    n_k_w.append(k_w[ki-1] * ki)

max = n_k_w[0]
for m in range(1, len(n_k_w)):
    if max < n_k_w[m]:
        max = n_k_w[m]

print(max)