import sys
sys.stdin = open('input.txt')

#
def blank_check():      # 빈 칸 있는지 체크
    for x in range(9):
        for y in range(9):
            if not sudoku[x][y]:
                return True
    return False

def squ(x, y):
    squ_visited = [-1] + [0] * 9
    squ_zero_cnt = 0
    squ_zero_idx = []

    for i in range(x, x+3):
        for j in range(y, y+3):
            if not sudoku[i][j]:
                squ_zero_cnt += 1
                squ_zero_idx.append((i, j))
            else:
                squ_visited[sudoku[i][j]] = 1

    if squ_zero_cnt == 1:
        for v in range(1, 10):
            if not squ_visited[v]:
                x, y = squ_zero_idx.pop()
                sudoku[x][y] = v

sudoku = [list(map(int, input().split())) for _ in range(9)]

zero = []
for x in range(9):
    for y in range(9):
        if not sudoku[x][y]:
            zero.append((x, y))

print(zero)

while blank_check():
    # 가로 검사
    for i in range(9):
        row_visited = [-1] + [0] * 9
        row_zero_cnt = 0
        row_zero_idx = []
        for j in range(9):
            if not sudoku[i][j]:
                row_zero_cnt += 1
                row_zero_idx.append((i, j))
            else:
                row_visited[sudoku[i][j]] = 1

        if row_zero_cnt == 1:
            for v in range(1, 10):
                if not row_visited[v]:
                    x, y = row_zero_idx.pop()
                    sudoku[x][y] = v

    if not blank_check():
        break

    # 세로 검사
    for i in range(9):
        col_visited = [-1] + [0] * 9
        col_zero_cnt = 0
        col_zero_idx = []
        for j in range(9):
            if not sudoku[j][i]:
                col_zero_cnt += 1
                col_zero_idx.append((j, i))
            else:
                col_visited[sudoku[j][i]] = 1

        if col_zero_cnt == 1:
            for v in range(1, 10):
                if not col_visited[v] and col_zero_idx:
                    x, y = col_zero_idx.pop()
                    sudoku[x][y] = v

    if not blank_check():
        break

    # 3x3 검사
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            squ(i, j)

for i in range(9):
    print(*sudoku[i])


    # def row_check(x):
    #     print(x)
    #
    #     for y in range(9):
    #         print(sudoku[x][y])
    #
    #     if x+1 < 9:
    #         row_check(x+1)