import sys
sys.stdin = open('input.txt')


def recur(start, cnt, sum, n):
    global min_v

    if sum > min_v:
        return

    if cnt == N:
        if W[n][start]:
            sum += W[n][start]
            min_v = min(min_v, sum)

    for i in range(N):
        if W[n][i] and not v[i]:
            v[i] = 1
            recur(start, cnt+1, sum+W[n][i], i)
            v[i] = 0

N = int(input())
W = [list(map(int, input().split())) for _ in range(N)]

v = [0]*N
min_v = 2147000000

for i in range(N):
    v[i] = 1
    recur(i, 1, 0, i)
    v[i] = 0

print(min_v)



'''
def sol(f, sum, cnt, start):
    global N, min_v

    if sum >= min_v:        # 백트래킹 (순회 도중 이미 sum이 min_v 보다 크다면 그 경로는 가지 않음)
        return
    # print(f, sum, cnt)
    if cnt == (N-1):                    # 모든 도시 방문했다면 출발했던 도시(start)로 돌아갈건데
        if data[f][start]:              # f에서 start로 가는 비용이 있다면 (갈 수 없으면 비용 0)
            sum += data[f][start]
            # print(sum)
            min_v = min(min_v, sum)     # 최소값과 비교하여 초기화
        return                          # if문 통과했든 안했든 모든 도시 방문했으니 리턴

    for i in range(N):                      # f번 도시에서 갈 수 있는 곳 탐색
        if data[f][i] and not visited[i]:   # f에서 i로 갈 수 있고, i번 도시에 방문하지 않았다면
            visited[i] = 1
            sol(i, sum+data[f][i], cnt+1, start)
            visited[i] = 0

N = int(input())        # 도시 수
data = [list(map(int, input().split())) for _ in range(N)]

visited = [0] * N       # 도시 방문 체크
min_v = 10**9           # 최소 비용

for s in range(N):      # s번 도시에서 시작
    visited[s] = 1
    sol(s, 0, 0, s)
    visited[s] = 0

print(min_v)
'''