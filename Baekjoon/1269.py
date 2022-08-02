import sys
sys.stdin = open('input.txt')


A_cnt, B_cnt = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

print(len(A^B))