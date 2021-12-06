import sys
sys.stdin = open('input.txt')

N, S = map(int, input().split())    # N : 정수의 개수, S : 원소 더한 값
data = list(map(int, input().split()))

ans = 0

for i in range(1, (1<<len(data))):  # 1부터 시작해서 공집합 제외
    sum = 0
    for j in range(0, len(data)):
        if i & (1<<j):
            # print(data[j], end=' ')
            sum += data[j]
    # print()
    # print('sum', sum)
    if sum == S:
        ans += 1

print(ans)