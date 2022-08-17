import sys
sys.stdin = open('input.txt')


N = int(input())
M = int(input())
S = input()

i = cnt = ans = 0
while i < M-2:
    if S[i:i+3] == 'IOI':
        cnt += 1
        if cnt == N:
            ans += 1
            cnt -= 1
        i += 1
    else:
        cnt = 0
    i += 1

print(ans)



''' [50점]
N = int(input())
M = int(input())
S = input()

P = 'I' + 'OI'*N
len_P = len(P)

cnt = 0
for i in range(M-len_P+1):
    if S[i:i+len_P] == P:
        cnt += 1

print(cnt)
'''