import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


dic = {}
tot = 0
while True:
    tmp = input().strip()

    if not tmp:
        break

    if tmp in dic:
        dic[tmp] += 1
    else:
        dic[tmp] = 1

    tot += 1

new_dic = dict(sorted(dic.items()))

for k, v in new_dic.items():
    print(k, '%.4f' %(v/tot * 100))