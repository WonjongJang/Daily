import sys
import re
sys.stdin = open('input.txt')


exp = input()
exp_list = re.split('([-+])', exp)  # -, + 기준으로 split. 괄호 안에 넣으면 기준도 포함

stack = []
flag = ''
while exp_list:
    e = exp_list.pop(0)
    if e.isdigit(): # 숫자면
        if flag == '+': # 숫자 앞의 기호가 +일 경우
            stack[-1] += int(e)     # stack 마지막 요소에 더함
        else:           # 숫자 앞의 기호가 -이거나 초기값일 경우
            stack.append(int(e))    # stack에 추가 (괄호 치기)
    else:           # 숫자 아니면 flag에 기호 초기화
        if e == '+':
            flag = '+'
        else:
            flag = '-'

ans = stack[0]
for s in range(1, len(stack)):  # stack에 남은 값들 모두 빼줌
    ans -= stack[s]

print(ans)