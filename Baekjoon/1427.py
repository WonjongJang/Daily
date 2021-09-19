import sys
sys.stdin = open('input.txt')

N = list(input())

N.sort(reverse=True)

print(''.join(N))