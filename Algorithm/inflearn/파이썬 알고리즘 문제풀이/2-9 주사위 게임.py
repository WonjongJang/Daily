import sys
sys.stdin = open('1-9 input.txt', 'rt')


# 전체 반복 횟수
T = int(input())

# 전체 반복
for tc in range(1, T+1):
    N = int(input())    # 참여하는 사람 수
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_v = 0
    for i in range(N):      # 사람마다
        cnt = [0] * 7       # 나온 주사위 눈 횟수 저장
        tot = 0             # 상금
        for j in range(3):
            cnt[arr[i][j]] += 1

        if 3 in cnt:    # 같은 눈 3개 존재할 때
            tot = 10000 + (cnt.index(3) * 1000)
        elif 2 in cnt:  # 같은 눈 2개 존재할 때
            tot = 1000 + (cnt.index(2) * 100)
        else:
            for k in range(6, 0, -1):
                if cnt[k] == 1:
                    tot = k * 100
                    break

        max_v = max(max_v, tot)

    print(max_v)



''' [풀이]
max=0
res=0
n=int(input())
for i in range(n):
    tmp=input().split() 
    tmp.sort() 
    a, b, c=map(int, tmp)
    if a==b and b==c:
        money=10000+(a*1000);
    elif a==b or a==c:
        money=1000+(a*100)
    elif b==c:
        money=1000+(b*100)
    else:
        money=c*100
    if money > res:
        res=money

print(res)
'''