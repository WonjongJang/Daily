msg = "It is Time"
print(msg.upper())
print(msg.lower())
print(msg)
tmp = msg.upper()
print(tmp)
print(tmp.find('T'))    # 앞에서부터 탐색하여 처음 만난 인덱스 반환
print(tmp.count('T'))
print(msg)
print(msg[:2])
print(msg[3:5])
print(len(msg))

for i in range(len(msg)):
    print(msg[i], end='')
print()

for x in msg:
    print(x, end='')
print()

for x in msg:
    if x.isupper():
        print(x, end=' ')
print()

for x in msg:
    if x.islower():
        print(x, end=' ')
print()

for x in msg:
    if x.isalpha():
        print(x, end='')
print()

tmp = "AZ"
for x in tmp:
    print(ord(x))

tmp = "az"
for x in tmp:
    print(ord(x))

tmp = 66
print(chr(tmp))