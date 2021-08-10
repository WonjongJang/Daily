a, b = input().split()

a = int(a[::-1])
b = int(b[::-1])

if a > b:
    print(a)
if a < b:
    print(b)