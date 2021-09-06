import sys
sys.stdin = open('input.txt')

K = int(input())

write = []
for k in range(K):
    money = int(input())
    if money:
        write.append(money)
    else:
        write.pop()

ans = 0
if write:
    ans = sum(write)

print(ans)