import sys
sys.stdin = open('3-1 input.txt', 'rt')


# 전체 반복 횟수
T = int(input())

# 전체 반복
for tc in range(1, T+1):
    words = input()
    leng = len(words)

    arr = list(words.lower())   # 모두 소문자로 변환 후 리스트로 저장

    if leng % 2:        # 홀수
        f = arr[:leng//2]
        e = arr[leng//2+1:leng]
        e.reverse()
        if f == e:
            ans = "YES"
        else:
            ans = "NO"
    else:               # 짝수
        f = arr[:leng//2]
        e = arr[leng//2:leng]
        e.reverse()
        if f == e:
            ans = "YES"
        else:
            ans = "NO"

    print("#{} {}".format(tc, ans))



''' [풀이1]
n=int(input())
for i in range(1, n+1):
    str=input()
    str=str.upper()
    for j in range(len(str)//2):
        if str[j]!=str[-1-j]:
            print("#%d NO" %i)
            break
    else:
        print("#%d YES" %i)
'''

''' [풀이2]
n=int(input())
for i in range(n):
    str=input()
    str=str.upper()
    if str==str[::-1]:
        print("#%d YES" %i)
    else:
        print("#%d NO" %i)
'''