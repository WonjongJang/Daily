import sys
sys.stdin = open('input.txt')

N = int(input())
info = {}   # 연락망
ans = 0 # 호석이가 정보들을 구매하는 데에 쓴 돈의 총합
for _ in range(N):
    query = input().split()

    if query[0] == '1': # 쿼리 1로 시작 (고릴라가 가진 정보)
        if query[1] in info:    # 기존 고릴라의 추가 정보
            temp = info[query[1]] + list(map(int, query[3:]))
            temp.sort(reverse=True)
            info[query[1]] = temp
        else:   # 새로운 고릴라의 정보
            temp = list(map(int, query[3:]))
            temp.sort(reverse=True)
            info[query[1]] = temp
    else:   # 쿼리 2로 시작 (호석이가 구매하는 정보)
        if query[1] in info:    # 연락망에 있는 정보
            cnt = 0
            while (len(info[query[1]])):    # 고릴라가 가진 정보가 더 적을 경우 대비
                if cnt == int(query[2]):
                    break
                ans += info[query[1]].pop(0)    # 한 번 거래한 정보는 파기
                cnt += 1
print(ans)