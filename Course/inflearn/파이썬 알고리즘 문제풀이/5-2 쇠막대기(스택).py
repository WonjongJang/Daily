import sys
sys.stdin = open('5-2 input.txt', 'rt')


# 전체 반복 횟수
T = int(input())

# 전체 반복
for tc in range(1, T+1):
    arr = input()

    ans = 0
    stack = []
    for i in range(len(arr)):
        if arr[i] == "(":
            stack.append(arr[i])
        else:
            if arr[i-1] == "(":
                stack.pop()
                ans += len(stack)
            else:
                stack.pop()
                ans += 1

    print(ans)



''' [풀이]
s=input()
stack=[]
cnt=0
for i in range(len(s)):
    if s[i]=='(':
        stack.append(s[i])
    else:
        stack.pop()
        if s[i-1]=='(':
            cnt+=len(stack)
        else:
            cnt+=1
print(cnt)
'''