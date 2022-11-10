import sys
sys.stdin = open('input.txt')


N = int(input())
for tc in range(N):
    s = list(input().split())

    ans = []
    while s:
        tmp = s.pop()
        ans.append(tmp)

    print('Case #{}: {}'.format(tc+1, ' '.join(ans)))