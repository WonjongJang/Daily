import sys
sys.stdin = open('input.txt')


N = int(input())    # 정수

x = N
ans = []
for i in range(2, N+1):
    if i * i > N:
        break

    while x % i == 0:
        print(i)
        x //= i

if x != 1:
    print(x)