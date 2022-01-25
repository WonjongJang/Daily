import sys
sys.stdin = open('input.txt')


while True:
    n = int(input())    # 자연수

    if not n:
        break

    # print(n)
    m = 2*n
    is_prime = [1 for _ in range(m+1)]  # 1부터 m까지 모두 소수라고 가정
    is_prime[1] = 0     # 1은 소수가 아니라고 미리 선언

    for i in range(2, m+1):
        if i*i > m:
            break

        if not is_prime[i]:
            continue

        for j in range(i*i, m+1, i):
            is_prime[j] = 0

    cnt = 0
    for k in range(n+1, m+1):
        if is_prime[k]:
            cnt += 1

    print(cnt)