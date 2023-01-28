import sys
sys.stdin = open('input.txt')


def findIdx(el):    # 이분 탐색
    s = 0
    e = len(LIS)-1

    while s <= e:
        m = (s+e)//2

        if LIS[m] == el:
            return m
        elif LIS[m] < el:
            s = m+1
        else:
            e = m-1

    return s

N = int(input())
A = list(map(int, input().split()))

LIS = [A[0]]    # 가장 긴 증가하는 부분 수열

for a in A:
    if LIS[-1] < a: # 요소가 더 크면 LIS에 추가
        LIS.append(a)
    else:           # 요소가 같거나 작다면
        idx = findIdx(a)    # LIS에서 어떤 인덱스에 넣을지 찾기
        LIS[idx] = a

print(len(LIS))
