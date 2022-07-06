import sys
from collections import deque
sys.stdin = open('4-9 input.txt', 'rt')


# 전체 반복 횟수
T = int(input())

# 전체 반복
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    arr = deque(arr)

    num = [0]
    d = ''
    while True:
        if arr[0] > num[-1] and arr[-1] > num[-1]:
            if arr[0] > arr[-1]:
                num.append(arr.pop())
                d += 'R'
            else:
                num.append(arr.popleft())
                d += 'L'
        elif arr[0] > num[-1] and arr[-1] < num[-1]:
            num.append(arr.popleft())
            d += 'L'
        elif arr[0] < num[-1] and arr[-1] > num[-1]:
            num.append(arr.pop())
            d += 'R'
        else:
            break

    print(len(num[1:]))
    print(d)



''' [풀이]
n=int(input())
a=list(map(int, input().split()))
lt=0
rt=n-1
last=0
res=""
tmp=[]
while lt<=rt:
    if a[lt]>last:
        tmp.append((a[lt], 'L'))
    if a[rt]>last:
        tmp.append((a[rt], 'R'))
    tmp.sort()
    if len(tmp)==0:
        break;
    else:
        res=res+tmp[0][1]
        last=tmp[0][0]
        if tmp[0][1]=='L':
            lt=lt+1
        else:
            rt=rt-1
    tmp.clear()

print(len(res))
print(res)
'''