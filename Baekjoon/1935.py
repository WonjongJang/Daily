import sys
sys.stdin = open('input.txt')

alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

N = int(input())
data = list(input())
print(data)
for _ in range(N):
    value = input()
    for d in range(len(data)):
        if data[d] in alpha:
            data[d] = value
            break

print(data)