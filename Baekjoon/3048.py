import sys
sys.stdin = open('input.txt')


N1, N2 = map(int, input().split())
n1 = input()
n2 = input()
T = int(input())

N = N1+N2
data = list(n1[::-1]+n2)

for t in range(T):
    for i in range(N-1):
        if data[i] in n1 and data[i+1] in n2:
            data[i], data[i+1] = data[i+1], data[i]

            if data[i+1] == n1[0]:
                break

print(''.join(data))