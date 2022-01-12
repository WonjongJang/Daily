import sys
sys.stdin = open('input.txt')


M = int(input())
N = int(input())

is_prime = [1 for _ in range(N+1)]
is_prime[1] = 0

for i in range(2, N+1):
    if i * i > N:
        break

    if not is_prime[i]:
        continue

    for j in range(i*i, N+1, i):
        is_prime[j] = 0

sum = 0
flag = 0
for p in range(M, N+1):
    if is_prime[p]:
        if not flag:
            min = p
            flag = 1
        sum += p

if not sum:
    print(-1)
else:
    print(sum)
    print(min)