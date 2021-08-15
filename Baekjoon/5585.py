money = int(input())
change = 1000 - money

c = [500, 100, 50, 10, 5, 1]

cnt = 0
for i in range(len(c)):
    while True:
        if change - c[i] > 0:
            change -= c[i]
            cnt += 1
        elif change - c[i] == 0:
            change -= c[i]
            cnt += 1
            break
        else:
            break

print(cnt)