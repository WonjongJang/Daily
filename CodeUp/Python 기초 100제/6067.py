num1 = int(input())

if num1 < 0:
    if num1 % 2 == 0:
        print('A')
    else:
        print('B')
else:
    if num1 % 2 == 0:
        print('C')
    else:
        print('D')