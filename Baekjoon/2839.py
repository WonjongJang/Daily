kg = int(input())

b1 = 5
b2 = 3

cnt = 0
while True:
    if kg % b1kg - b1 > 0:
        kg -= b1
        cnt += 1
        if kg % b2 == 0 and kg - b2 > 0:
            kg -= b2
            cnt += 1
        elif kg % b2 == 0 and kg - b2 == 0:
            kg -= b2
            cnt += 1
            ans = cnt
            break
        elif kg - b1 == 0:
            kg -= b1
            cnt += 1
            ans = cnt
            break
    else:
        ans = cnt
        break

if kg != 0:
    ans = -1

print(ans)