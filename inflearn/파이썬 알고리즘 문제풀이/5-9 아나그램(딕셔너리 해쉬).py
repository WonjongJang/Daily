import sys
sys.stdin = open('5-9 input.txt', 'rt')


# 전체 반복 횟수
T = int(input())

# 전체 반복
for tc in range(1, T+1):
    word1 = input()
    word2 = input()

    d1 = {w: 0 for w in word1}
    for w1 in word1:
        d1[w1] += 1

    d2 = {w: 0 for w in word2}
    for w2 in word2:
        d2[w2] += 1

    if d1 == d2:
        print("YES")
    else:
        print("NO")



''' [풀이]
a=input()
b=input()
sH=dict()
for x in a:
    sH[x]=sH.get(x, 0)+1
for x in b:
    sH[x]=sH.get(x, 0)-1

for x in a:
    if(sH.get(x)>0):
        print("NO")
        break;
else:
    print("YES")
'''