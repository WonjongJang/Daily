'''
a = range(1, 11)
print(list(a))

for i in range(1, 11):
    print(i)

for i in range(10, 0, -1):
    print(i)

i = 1
while i <= 10:
    print(i)
    i = i+1

i = 10
while i >= 1:
    print(i)
    i = i-1

i = 1
while True:
    print(i)
    if i == 5:
        break
    i += 1

for i in range(1, 11):
    if i%2 == 0:
        continue
    print(i)
'''
for i in range(1, 11):
    print(i)
    if i > 15:
        break
else:   # range 모두 돌았을때만 실행
    print(11)