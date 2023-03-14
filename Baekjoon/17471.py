import sys
sys.stdin = open('input.txt')


def bfs(arr):
    que = [arr[0]]
    v = [0] * (N+1) # 방문 처리
    v[arr[0]] = 1

    cnt = 0
    sum = 0 # 인구 합계
    while que:
        x = que.pop(0)  # x 구역
        cnt += 1
        sum += P[x]
        for i in adj[x]:    # x 구역과 인접한 구역
            if i in arr and not v[i]:
                que.append(i)
                v[i] = 1

    if cnt == len(arr):
        return sum
    else:   # cnt와 arr 길이가 맞지 않는다면 나눈 선거구의 구역들이 인접하지 않은 것
        return 0



def dfs(x): # 부분 집합 만드는 함수
    global min_v

    if x == N+1:
        A, B = [], []   # A, B 선거구
        for i in range(1, len(S)):
            if S[i]:
                A.append(i)
            else:
                B.append(i)

        if len(A) and len(B):   # 선거구는 구역을 적어도 하나 포함해야 함 (공집합 X)
            a = bfs(A)  # A 선거구 인구 합계
            b = bfs(B)  # B 선거구 인구 합계
            if a and b:
                min_v = min(min_v, abs(a-b))
    else:
        S[x] = 1
        dfs(x+1)
        S[x] = 0
        dfs(x+1)

N = int(input())    # 구역의 개수
P = [0] + list(map(int, input().split()))   # 각 구역의 인구
adj = [[]]  # 각 구역과 인접한 구역
for _ in range(N):
    temp = list(map(int, input().split()))
    adj.append(temp[1:])

min_v = 100000  # 최소값 초기화
S = [0] * (N+1) # 부분 집합
dfs(1)

if min_v == 100000: # 두 선거구로 나눌 수 있는 방법이 없는 경우
    print(-1)
else:
    print(min_v)