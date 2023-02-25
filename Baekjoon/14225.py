import sys
sys.stdin = open('input.txt')


def recur(n):
    if n == N:
        sum = 0
        for i in range(N):
            if v[i]:
                sum += S[i]
        sum_list.append(sum)
    else:
        v[n] = 1
        recur(n+1)
        v[n] = 0
        recur(n+1)

N = int(input())
S = list(map(int, input().split()))
v = [0]*N
sum_list = []   # 모든 부분 수열의 합을 담음

recur(0)    # 부분 집합 구하기

sum_list = list(set(sum_list))  # 중복값 제거
sum_list.sort() # 정렬
for i in range(len(sum_list)):  # 정렬된 부분 수열의 합들을 i=0 부터 비교해 봄
    if i != sum_list[i]:    # 해당 인덱스에 같은 값이 없다면 그 값이 없는 것이므로 나올 수 없는 가장 작은 수가 됨
        print(i)
        break
else:
    print(i+1)  # 모든 값이 있다면 sum_list의 max 값보다 1 큰 값이 정답