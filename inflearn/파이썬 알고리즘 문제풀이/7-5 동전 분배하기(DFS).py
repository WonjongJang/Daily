import sys
sys.stdin = open('7-5 input.txt')


def recur(L):
    global min_v

    if L == N:
        if len(set(tot)) != 3:
            return
        min_v = min(min_v, max(tot)-min(tot))
        return

    for i in range(3):
        tot[i] += coins[L]
        recur(L+1)
        tot[i] -= coins[L]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    coins = []
    for _ in range(N):
        coins.append(int(input()))

    tot = [0] * 3
    min_v = 2147000000
    recur(0)

    print(min_v)



''' [풀이]
def DFS(L):
    global res
    if L==n:
        cha=max(money)-min(money)
        if cha<res:
            tmp=set()
            for x in money:
                tmp.add(x)
            if len(tmp)==3:
                res=cha
    else:
        for i in range(3):
            money[i]+=coin[L]
            DFS(L+1)
            money[i]-=coin[L]

n=int(input())
coin=[]
tmp=[]
money=[0]*3
res=2147000000
for _ in range(n):
    coin.append(int(input()))
DFS(0)
print(res)
'''