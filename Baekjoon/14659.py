import sys
sys.stdin = open('input.txt')


N = int(input())
data = list(map(int, input().split()))

max_data = 0
cnt = 0
ans = 0
for d in data:
    if d > max_data:
        max_data = d
        cnt = 0
    else:
        cnt += 1
    ans = max(ans, cnt)

print(ans)



''' 시간초과
N = int(input())
data = list(map(int, input().split()))

max_v = 0
for i in range(N):
    cnt = 0
    # print(data[i])
    for j in range(i+1, N):
        if data[i] < data[j]:
            break
        cnt += 1
    max_v = max(max_v, cnt)

print(max_v)
'''