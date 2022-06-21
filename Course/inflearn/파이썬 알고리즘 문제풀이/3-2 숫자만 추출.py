import sys
sys.stdin = open('3-2 input.txt', 'rt')


# 전체 반복 횟수
T = int(input())

# 전체 반복
for tc in range(1, T+1):
    str = input()

    num = ''
    for i in str:
        if i.isdecimal():
            num += i

    num = int(num)

    cnt = 0
    for j in range(1, num+1):
        if not num % j:
            cnt += 1

    print(num)
    print(cnt)



''' [풀이]
s=input()
res=0
for x in s:
    if x.isdecimal():
        res=res*10+int(x)
print(res)
cnt=0
for i in range(1, res+1):
    if res%i==0:
        cnt+=1
print(cnt)
'''