import sys
sys.stdin = open('input.txt')


S = input()

dic = {}
for i in range(0, len(S)):
    for j in range(1, len(S)+1):
        if S[i:j]:
            if S[i:j] not in dic:
                dic[S[i:j]] = 1
            else:
                dic[S[i:j]] += 1

print(len(dic))