import sys
sys.stdin = open('input.txt')

def is_prime(x, tmp, cnt):
    if cnt == N:
        print(x)
        return

    if tmp == 1:
        return

    flag = 1
    for i in range(2, tmp+1):
        if i * i > tmp:
            break

        if tmp % i == 0:
            flag = 0
            break
    if flag:
        # print(tmp, "소수")
        is_prime(x, tmp//10, cnt+1)
    else:
        # print(tmp, "소수아님")
        return

N = int(input())    # 자리수

if N == 1:
    start = 2
    end = 10
else:
    start = 10 ** (N-1)
    end = start * 10

# print(start, end)
for r in range(start, end):
    is_prime(r, r, 0)



# 메모리 초과
# N = int(input())    # 자리수
#
# if N == 1:
#     start = 2
#     end = 10
# else:
#     start = 10 ** (N-1)
#     end = start * 10
#
# is_prime = [1 for _ in range(end+1)]
# is_prime[1] = 0
#
# for i in range(2, end+1):
#     if i*i > end:
#         break
#
#     if not is_prime[i]:
#         continue
#
#     for j in range(i*i, end+1, i):
#         is_prime[j] = 0
#
# for k in range(start, end+1):
#     if is_prime[k]:
#         # print(k)
#         check = 1
#         tmp = k
#         while tmp:
#             # print(k)
#             tmp //= 10
#             if not is_prime[tmp]:
#                 check = 0
#                 break
#
#         if check:
#             is_prime[k] = 2
#
# for p in range(start, end+1):
#     if is_prime[p] == 2:
#         print(p)