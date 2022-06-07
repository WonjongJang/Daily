n = int(input())

# 1) 1부터 n까지 홀수출력하기
for i in range(1, n+1):
    if i%2:
        print(i)

# 2) 1부터 n까지의 합 구하기
sum = 0
for i in range(1, n+1):
    sum += i
print(sum)

# 3) n의 약수출력하기
for i in range(1, n+1):
    if not n%i:
        print(i, end=' ')