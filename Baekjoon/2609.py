import sys
sys.stdin = open('input.txt')


A, B = map(int, input().split())    # 두 개의 자연수

temp = A * B

while A % B != 0:
    A, B = B, A % B

LCM = temp // B

print(B)
print(LCM)