import sys
sys.stdin = open('input.txt')

N = int(input())

i = 1
cnt = 0
while cnt < N:
    same = False

    if i // 10:
        str_i = str(i)
        for c1 in range(len(str_i)-1):
            for c2 in range(c1+1, len(str_i)):
                if str_i[c1] == str_i[c2]:
                    i += 1
                    same = True
                    break

    if same == False:
        print(i)
        cnt += 1
        i += 1