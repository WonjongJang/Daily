a = [23, 12, 36, 53, 19]
print(a[:3])
print(a[1:4])
print(len(a))

for i in range(len(a)):
    print(a[i], end=' ')
print()

for x in a:
    print(x, end=' ')
print()

for x in a:
    if x%2 == 1:
        print(x, end=' ')
print()

for x in enumerate(a):  # (index, value) 튜플 형태
    print(x)

b = (1, 2, 3, 4, 5)
print(b[0])
# b[0] = 7    # 튜플은 리스트처럼 값 변경 불가

for x in enumerate(a):
    print(x[0], x[1])
print()

for index, value in enumerate(a):
    print(index, value)
print()

if all(60 > x for x in a):  # 모두 참일 때
    print("YES")
else:
    print("NO")

if any(11 > x for x in a):  # 한 개라도 참일 때
    print("YES")
else:
    print("NO")