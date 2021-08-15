S = input()

alpha = [
    'a', 'b', 'c', 'd', 'e',
    'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z'
    ]
c = [-1] * 26

for s in range(len(S)): #baekjoon # 0
    for a in range(len(alpha)): # 1
        if S[s] == alpha[a] and c[a] == -1:
            c[a] = s

print(*c)
