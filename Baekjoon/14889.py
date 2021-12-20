import sys
sys.stdin = open('input.txt')


def cal(s, l):
    global min_v

    sum_s = 0       # 스타트 팀 능력치 합
    for i in s:
        for j in s:
            sum_s += data[i-1][j-1]
    # print(sum_s)

    sum_l = 0       # 링크 팀 능력치 합
    for i in l:
        for j in l:
            sum_l += data[i-1][j-1]
    # print(sum_l)

    min_v = min(min_v, abs(sum_s-sum_l))

def nCr(n, r, s, cnt):
    if cnt == r:
        link = []   # 링크 팀
        for i in range(N):
            if people[i] not in start:  # 사람 리스트에서 start 팀에 속해있지 않은 사람
                link.append(people[i])  # 링크 팀에 추가
        # print(start, link)
        cal(start, link)
    else:
        for i in range(s, n-r+cnt+1):
            start[cnt] = people[i]
            nCr(n, r, i+1, cnt+1)

N = int(input())    # 인원
data = [list(map(int, input().split())) for _ in range(N)]  # 능력치

people = list(range(1, N+1))    # 사람 리스트
R = N//2    # 팀 인원 수

start = [0] * R     # 스타트 팀
min_v = 100000

nCr(N, R, 0, 0)

print(min_v)