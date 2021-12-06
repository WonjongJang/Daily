import sys
sys.stdin = open('input.txt')

N = int(input())    # 회의의 수
info = [list(map(int, input().split())) for n in range(N)]


print(info)