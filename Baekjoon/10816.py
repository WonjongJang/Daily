import sys
sys.stdin = open('input.txt')


N = int(input())
cards = list(map(int, input().split()))
M = int(input())
data = list(map(int, input().split()))

dic = {}
for card in cards:
    if card in dic:
        dic[card] += 1
    else:
        dic[card] = 1

for d in data:
    if d in dic:
        print(dic[d], end=' ')
    else:
        print(0, end=' ')



'''
N = int(input())
N_list = list(map(int, input().split()))
M = int(input())
M_list = list(map(int, input().split()))

dic = {}
for n in N_list:
    if n in dic:
        dic[n] += 1
    else:
        dic[n] = 1

for m in M_list:
    if m in dic:
        print(dic[m], end=" ")
    else:
        print(0, end=" ")
'''