import sys
sys.stdin = open('6-2 input.txt', 'rt')


def recur(v):
    if v > 7:
        return
    else:
        # print(v, end=" ")     # 전위순회
        recur(v*2)
        # print(v, end=" ")     # 중위순회
        recur(v*2+1)
        # print(v, end=" ")     # 후위순회

# 전체 반복 횟수
T = int(input())

# 전체 반복
for tc in range(1, T+1):
    recur(1)



''' [풀이]

'''