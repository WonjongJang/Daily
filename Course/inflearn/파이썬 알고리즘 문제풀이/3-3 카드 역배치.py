import sys
sys.stdin = open('3-3 input.txt', 'rt')


# 전체 반복 횟수
T = int(input())

# 전체 반복
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(10)]

    cards = list(range(1, 21))

    for i in range(10):
        s, e = arr[i]

        tmp = cards[s-1:e]
        tmp.reverse()

        for j in range(s-1, e):
            cards[j] = tmp[j-s+1]


    print(*cards)



''' [풀이]
a=list(range(21))
for _ in range(10):
    s, e=map(int, input().split())
    for i in range((e-s+1)//2):
        a[s+i], a[e-i]=a[e-i], a[s+i]
a.pop(0)
for x in a:
    print(x, end=' ')
'''