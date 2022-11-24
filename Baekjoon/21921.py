import sys
sys.stdin = open('input.txt')


N, X = map(int, input().split())
data = list(map(int, input().split()))

tmp = sum(data[:X])
max_v = tmp
cnt = 1

for i in range(N-X):
    tmp = tmp - data[i] + data[i+X]
    if tmp > max_v:
        max_v = tmp
        cnt = 1
    elif tmp == max_v:
        cnt += 1

if max_v:
    print(max_v)
    print(cnt)
else:
    print('SAD')



''' 시간초과
N, X = map(int, input().split())
data = list(map(int, input().split()))

max_v = 0
cnt = 0
for i in range(X-1, N):
    tmp = sum(data[i-X+1:i+1])
    if tmp > max_v:
        max_v = tmp
        cnt = 1
    elif tmp == max_v:
        cnt += 1

if max_v:
    print(max_v)
    print(cnt)
else:
    print('SAD')
'''