N, K = map(int, input().split())

numbers = list(range(1, N+1))
q = []

while numbers:
    k = 0
    while True:
        k += 1

        if k == K:
            q.append(numbers.pop(0))
            break

        a = numbers.pop(0)
        numbers.append(a)

print('<{}>'.format(', '.join(map(str, q))))
