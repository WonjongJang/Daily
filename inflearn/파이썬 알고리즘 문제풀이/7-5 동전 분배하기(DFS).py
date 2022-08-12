import sys
sys.stdin = open('7-5 input.txt')


def recur(L, sum):
    global ans

    if sum > T:
        return
    if L == K:
        if sum == T:
            ans += 1
    else:
        for i in range(C[L][1]+1):
            recur(L+1, sum+(C[L][0]*i))

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    coins = []
    for _ in range(N):
        coins.append(int(input()))

    print(coins)
    print(sum(coins))


''' [풀이]

'''