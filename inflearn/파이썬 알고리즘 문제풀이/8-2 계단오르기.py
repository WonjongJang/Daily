import sys
sys.stdin = open('8-2 input.txt')


def recur(n):
    if n == 1:
        return 1
    if n == 2:
        return 2

    if memo[n] != -1:
        return memo[n]

    memo[n] = recur(n-1) + recur(n-2)

    return memo[n]

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    memo = [-1]*(N+1)

    print(recur(N))



''' [풀이]

'''