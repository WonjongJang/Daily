import sys
sys.stdin = open('1-7 input.txt', 'rt')


# 전체 반복 횟수
T = int(input())

# 전체 반복
for tc in range(1, T+1):
    N = int(input())    # 자연수

    is_prime = [1] * (N+1)
    is_prime[1] = 0

    for i in range(2, N+1):
        if i*i > N:
            break

        if not is_prime[i]:
            continue

        for j in range(i*i, N+1, i):
            if is_prime[j]:
                is_prime[j] = 0

    cnt = 0
    for c in range(1, N+1):
        if is_prime[c]:
            cnt += 1

    print(cnt)