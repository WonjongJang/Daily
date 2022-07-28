import sys
sys.stdin = open('input.txt')


N, M = map(int, input().split())
dic = {}
ans = []
for _ in range(N+M):
    name = input()
    if name in dic:
        dic[name] += 1
        ans.append(name)
    else:
        dic[name] = 1

ans.sort()

print(len(ans))
for a in ans:
    print(a)
