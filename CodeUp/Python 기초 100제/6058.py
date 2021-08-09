num1, num2 = input().split()

b1 = bool(int(num1))
b2 = bool(int(num2))

if b1 == False and b2 == False:
    print(True)
else:
    print(False)