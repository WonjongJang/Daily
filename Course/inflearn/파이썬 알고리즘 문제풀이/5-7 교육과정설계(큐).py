import sys
sys.stdin = open('5-7 input.txt', 'rt')


# 전체 반복 횟수
T = int(input())

# 전체 반복
for tc in range(1, T+1):
    E = list(input())
    N = int(input())
    arr = [input() for _ in range(N)]

    for i in range(N):
        Q = E[::]
        for x in arr[i]:
            if Q and x == Q[0]:
                Q.pop(0)

        if Q:
            print("#{} NO".format(i+1))
        else:
            print("#{} YES".format(i+1))



''' [풀이]
need=input()
n=int(input())
for i in range(n):
    plan=input()
    dq=deque(need)
    for x in plan:
        if x in dq:
            if x!=dq.popleft():
                print("#%d NO" %(i+1))
                break
    else:
        if len(dq)==0:
            print("#%d YES" %(i+1))
        else:
            print("#%d NO" %(i+1))
'''