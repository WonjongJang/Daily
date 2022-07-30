import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


N, M = map(int, input().split())
dic1 = {}
dic2 = {}
for n in range(N):
    str_N = str(n+1)
    poke = input().strip()
    dic1[poke] = str_N
    dic2[str_N] = poke

for _ in range(M):
    quest = input().strip()
    if quest.isdecimal():
        print(dic2[quest])
    else:
        print(dic1[quest])



''' 시간 초과
N, M = map(int, input().split())
dic = {}
for n in range(N):
    poke = input()
    dic[poke] = str(n+1)

for _ in range(M):
    quest = input()
    if quest.isdecimal():
        for k, v in dic.items():
            if quest == v:
                print(k)
    else:
        print(dic[quest])
'''