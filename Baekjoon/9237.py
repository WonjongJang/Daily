import sys
sys.stdin = open('input.txt')

N = int(input())    # 묘목의 수
T = list(map(int, input().split())) # 각 나무 자라는 일수

T.sort(reverse=True)    # 자라는 데 오래 걸리는 나무 부터 심어야 하기 때문에 내림차순 정렬

max_list = []
for i in range(N):
    max_list.append((i+1) + T[i])

print(max(max_list) + 1)