import sys
sys.stdin = open('5-8 input.txt', 'rt')


# 전체 반복 횟수
T = int(input())

# 전체 반복
for tc in range(1, T+1):
    N = int(input())
    words = dict()

    for i in range(N):
        word = input()
        words[word] = 0

    for j in range(N-1):
        poem = input()
        words[poem] = 1

    for k, v in words.items():
        if not v:
            print(k)
            break



''' [풀이]
n=int(input())
p=dict()
for i in range(n):
    word=input()
    p[word]=1
for i in range(n-1):
    word=input()
    p[word]=0
for key, val in p.items():
    if val==1:
        print(key)
        break
'''