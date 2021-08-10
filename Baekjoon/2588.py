num1 = int(input())
num2 = int(input())

c = num2
for i in range(3):
    print(num1 * (c % 10))
    c //= 10
print(num1 * num2)