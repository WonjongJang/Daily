import sys
sys.stdin = open('7-6 input.txt')


def recur(L):
    if L == leng:
        s = 0
        word = ''
        for a in arr:
            if code[s] == '0':
                return
            tmp = int(code[s:s+a])

            if tmp <= 26:
                word += chr(tmp+64)
            else:
                return
            s += a
        ans.append(word)

    if L > leng:
        return

    arr.append(1)
    recur(L+1)
    arr.pop()
    arr.append(2)
    recur(L+2)
    arr.pop()

T = int(input())
for tc in range(1, T+1):
    code = input()

    leng = len(code)
    arr = []
    ans = []
    recur(0)

    for x in ans:
        print(x)
    print(len(ans))


''' [풀이]

'''