import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())    # N : 문서 개수, M : 궁금한 문서
    documents = list(range(N))
    importance = list(map(int, input().split()))    # 중요도

    total = []
    for t in range(N):
        total.append([importance[t], documents[t]])

    # print(N, M)
    # print(documents)
    # print(importance)
    # print(total)

    cnt = 0
    while True:
        for i in range(1, len(total)):
            if total[0][0] < total[i][0]:
                back = total.pop(0)
                total.append(back)
                break
        else:
            output = total.pop(0)
            cnt += 1
            # print(output) # 디버깅
            if output[1] == M:
                break

    print(cnt)