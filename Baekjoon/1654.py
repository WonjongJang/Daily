import sys
sys.stdin = open('input.txt')


def check(m):
  temp = 0
  for kl in KList:
    temp += kl//m
  return temp

K, N = map(int, input().split())
KList = [int(input()) for _ in range(K)]

# 이분 탐색
l, r = 1, max(KList)  # l이 0인 경우 ZeroDivisionError
while l <= r:
  m = (l+r)//2  # m 크기로 랜선들을 자를 것

  cnt = check(m)  # 각 랜선들을 자른 총 개수

  if cnt < N: # 개수가 N 보다 작으면
    r = m-1     # 더 작게 잘라야 함
  else:       # 개수가 N과 같거나 크면 (N개보다 많이 만드는 것도 N개를 만드는 것에 포함이라는 문구 때문에 분기 X)
    l = m+1     # 더 크게 자름

print(r)



# function solution(k, n, kList) {
#   const checkKList = (m) => {
#     let cnt = 0;
#     for (i of kList) {
#       cnt += parseInt(i / m);
#     }
#     return cnt;
#   };
#
#   let l = 0;
#   let r = Math.min(...kList);
#   while (l <= r) {
#     m = parseInt((l + r) / 2);
#
#     let temp = checkKList(m);
#
#     if (temp < n) {
#       r = m - 1;
#     } else {
#       l = m + 1;
#     }
#   }
#   console.log(r);
# }
#
# console.log(solution(4, 11, [802, 743, 457, 539]));
