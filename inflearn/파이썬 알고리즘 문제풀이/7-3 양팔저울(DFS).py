import sys
sys.stdin = open('7-3 input.txt')


K = int(input())
K_list = list(map(int, input().split()))

print(K_list)
S = sum(K_list)
print(S)
S_list = list(range(1, S+1))
print(S_list)