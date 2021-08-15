N = int(input())
a = list(map(int, input().split()))

ans = 0
for i in range(N):
    count = 0
    for j in range(2, a[i]+1):  # 2부터 입력된 값까지 검사
        if a[i] != j and a[i] % j == 0:
            count = 1
    if a[i] > 1 and count == 0:
        ans += 1
print(ans)


