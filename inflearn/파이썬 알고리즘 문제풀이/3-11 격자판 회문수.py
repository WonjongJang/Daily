import sys
sys.stdin = open('3-11 input.txt', 'rt')


# 전체 반복 횟수
T = int(input())

# 전체 반복
for tc in range(1, T+1):
    arr = [list(map(str, input().split())) for _ in range(7)]

    cnt = 0
    for i in range(7):
        for j in range(7):
            word_r = ''
            word_c = ''
            for k in range(5):
                if 0 <= j+4 < 7:
                    word_r += arr[i][j+k]
                if 0 <= i+4 < 7:
                    word_c += arr[i+k][j]

            if word_r:
                if word_r == word_r[::-1]:
                    cnt += 1
            if word_c:
                if word_c == word_c[::-1]:
                    cnt += 1

    print(cnt)



''' [풀이]
board=[list(map(int, input().split())) for _ in range(7)]
cnt=0
for i in range(3):
    for j in range(7):
        tmp=board[j][i:i+5]
        if tmp==tmp[::-1]:
            cnt+=1
        for k in range(2):
            if board[i+k][j]!=board[i+5-k-1][j]:
                break;
        else:
            cnt+=1
        
print(cnt)
'''

''' [풀이 (회문의 길이가 가변적일 때)]
board=[list(map(int, input().split())) for _ in range(7)]
cnt=0
len=5
for i in range(3):
    for j in range(7):
        tmp=board[j][i:i+len]
        if tmp==tmp[::-1]:
            cnt+=1
        #tmp=board[i:i+5][j] 앞 행은 리스트가 아니라서 슬라이스가 안된다.
        for k in range(len//2):
            if board[i+k][j]!=board[len-k+i-1][j]:
                break;
        else:
            cnt+=1
        
print(cnt)
'''