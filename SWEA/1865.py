import sys
sys.stdin = open('input.txt')

import time
start = time.time()

def sol(x, y, P, cnt):
    global max_P

    if P == 0:                  # 일을 성공할 확률이 0인 것 거르기
        return

    if P <= max_P:              # 백트래킹 (할 일을 모두 소수로 받았기 때문에 P가 이미 max_P 보다 작아졌다면 가장 큰 확률인 1.0을 곱해도 더 커질 수 없음)
        return
    # print(x, y, P, cnt)

    if cnt == N:                # 모든 직원이 일을 선택했을 때
        max_P = max(max_P, P)   # max_P와 P 중 큰 값을 max_P에 저장
        return

    for j in range(N):
        if visited[j] == 0:
            visited[j] = 1
            sol(x+1, j, P * data[x+1][j], cnt+1)
            visited[j] = 0

# 전체 반복 횟수
T = int(input())

# 전체 반복
for tc in range(1, T+1):
    N = int(input())    # 직원 수, 할 일 수
    data = [list(map(lambda x: int(x)/100, input().split())) for _ in range(N)]

    # print(data)
    max_P = 0           # 최대 확률
    visited = [0] * N   # 남은 할 일 체크

    for j in range(N):  # 첫 번째 직원이 j번째 일을 선택할 경우
        visited[j] = 1
        sol(0, j, data[0][j], 1)
        visited[j] = 0

    ans = format(max_P * 100, '.6f')

    # 출력
    print('#{} {}'.format(tc, ans))

end = time.time()

print("WorkingTime: {} sec".format(end-start))