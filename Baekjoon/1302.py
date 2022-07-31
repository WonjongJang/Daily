import sys
sys.stdin = open('input.txt')


N = int(input())
dic = {}
for _ in range(N):
    book = input()
    if book in dic:
        dic[book] += 1
    else:
        dic[book] = 1

max_list = []
max_v = max(dic.values())
for k, v in dic.items():
    if v == max_v:
        max_list.append((k, v))

max_list.sort()

print(max_list[0][0])