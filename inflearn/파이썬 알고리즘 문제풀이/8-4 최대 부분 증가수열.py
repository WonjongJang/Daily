import sys
sys.stdin = open('8-4 input.txt')


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))

    data.sort()
    print(data)



''' [풀이]

'''