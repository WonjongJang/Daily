N = int(input())  # 사람의 수
Pi = list(map(int, input().split()))

# 오름차순 정렬
for s1 in range(N-1):
    min = s1
    for s2 in range(s1+1, N):
        if Pi[min] > Pi[s2]:
            min = s2
    Pi[s1], Pi[min] = Pi[min], Pi[s1]

# 누적 합
sum = 0
for i in range(N):
    for j in range(i+1):
        sum += Pi[j]

print(sum)