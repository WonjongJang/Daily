import sys
sys.stdin = open('input.txt')

data = input()

alphabet = [0] * 26     # ABCDE... 순서대로 인덱스 사용 (총 26개)

for i in range(len(data)):
    alphabet[ord(data[i]) - 65] += 1    # 순서대로 들어가게끔 아스키 코드 활용

odd_cnt = 0     # 홀수의 총 개수
odd = ''
even = ''
for j in range(26):
    if alphabet[j] % 2:         # 해당 알파벳의 개수가 홀수이면
        odd_cnt += 1            # 카운트
        odd += chr(j + 65)
    even += chr(j + 65) * (alphabet[j] // 2)    # else 처리 하지 않는 이유는 홀수일 때
                                                # 알파벳 개수가 1이 아니라 3이나 5, 그 이상일 경우 1개 빼고는 even에 넣어야 함
if odd_cnt > 1:                 # 홀수가 2개 이상이면
    print("I'm Sorry Hansoo")
else:
    print(even+odd+even[::-1])



# 시간 초과
# def palindrome(arr):
#     global l, bt
#
#     if l % 2:
#         if arr[:l//2] == arr[l:l//2:-1]:
#             print(''.join(arr))
#             bt = True
#             return
#     else:
#         if arr[:l//2] == arr[l:l//2-1:-1]:
#             print(''.join(arr))
#             bt = True
#             return
#
# def perm(n, k):
#     if bt:
#         return
#
#     if k == n:
#         palindrome(p)
#         # print(p)
#         return
#
#     for i in range(l):
#         if used[i] == 0:
#             used[i] = 1
#             p[k] = alpha[i]
#             perm(n, k+1)
#             used[i] = 0
#
# alpha = list(input())
# l = len(alpha)
#
# alpha.sort()
#
# bt = False
# p = [0] * l
# used = [0] * l
#
# perm(l, 0)
#
# if not bt:
#     print("I'm Sorry Hansoo")