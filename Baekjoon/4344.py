import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    a = list(map(int, input().split()))

    sum = 0     # 각 학생 점수 합
    mean = 0    # 평균
    for s in range(1, len(a)):
        sum += a[s]
    mean = sum / a[0]

    count = 0   # 평균 넘는 학생 수
    for i in range(1, len(a)):
       if a[i] > mean:  # 각 점수 > 평균
           count += 1
    
    p = (count / a[0]) * 100    # 비율
    print('{}{}'.format(format(p, '.3f'), '%'))