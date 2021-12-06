import sys
sys.stdin = open('input.txt')

M = int(input())    # 연산의 수
S = set()  # 공집합

for m in range(M):
    data = sys.stdin.readline().split()

    if len(data) > 1:
        num = int(data[1])

    # print(data)
    if data[0] == 'add':
        S.add(num)
    elif data[0] == 'remove':
        S.discard(num)  # remove를 쓰면 존재하지 않는 수 제거 시 에러 발생 -> discard는 에러 발생 X
    elif data[0] == 'check':
        if num in S:
            print(1)
        else:
            print(0)
    elif data[0] == 'toggle':
        if num in S:
            S.discard(num)
        else:
            S.add(num)
    elif data[0] == 'all':
        S = set(range(1, 21))
    elif data[0] == 'empty':
        S = set()