import sys
sys.stdin = open('input.txt')


T = int(input())
for _ in range(T):
    data = input()

    flag = 1
    stack = []
    for i in data:
        if i == '(':
            stack.append(i)
        else:
            if stack:
                stack.pop()
            else:
                flag = 0
                break

    if flag:
        if stack:
            print('NO')
        else:
            print('YES')
    else:
        print('NO')



'''
T = int(input())
for tc in range(1, T+1):
    PS = input()

    # print(PS)
    ans = "NO"
    case = 0    # stack이 비었을 때 )가 오는 case

    # (로 시작하는 경우
        # 딱 맞을 경우  -> YES
        # (가 남을 경우 -> NO
        # )가 많을 경우 -> NO
    # )로 시작하는 경우 -> NO

    stack = []
    for i in PS:
        if i == '(':        # ( 일 때
            stack.append(i)     # stack에 넣음
        else:               # ) 일 때
            if stack:           # stack에 (가 있다면
                stack.pop()         # stack에서 가장 뒤에 있는 ( 뺌
            else:               # stack에 (가 없다면
                case = 1
                break               # NO

    if not stack and not case:  # 검사 후 stack이 비어 있고 case가 아니라면
        ans = "YES"

    print(ans)
'''



'''
T = int(input())

for t in range(T):
    stack = []
    ps = input()
    if ps[0] == ')':    # )로 시작하는 경우
        print('NO')
        continue
    for i in range(len(ps)):
        if ps[i] == '(':
            stack.append(ps[i])
        else:
            if stack:
                stack.pop()
            else:
                stack.append(ps[i])
                break
    if stack:
        print('NO')
    else:
        print('YES')
'''