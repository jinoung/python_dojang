row, col = map(int, input().split())
matrix = []
for i in range(row):
    matrix.append(list(input()))

# 인접한 지뢰의 개수를 계산하여 matrix 업데이트
# 1. 지뢰가 있는 위치 검사
#   현재 위치에서 좌우상하의 위치에 * 있으면 지뢰갯수 증가
#   col == 0 이면 left는 확인하지 않음
#   col == end 이면 right는 확인하지 않음
#   row == 0 이면 upper는 확인하지 않음
#   row == end 이면 down은 확인하지 않음
for i in range(col):
    for j in range(row):
        mine = 0
        if matrix[i][j] == '.':
            #print("i=",i, " j=",j)
            if j != row-1:
                if matrix[i][j+1] == '*': #right
                    #print("right.i=",i," j=",j)
                    mine += 1
            if j != 0:
                if matrix[i][j-1] == '*': #left
                    #print("left.i=",i," j=",j)
                    mine += 1
            if i != col-1:
                if matrix[i+1][j] == '*': #upper
                    #print("upper.i=",i," j=",j)
                    mine += 1
            if i != 0:
                if matrix[i-1][j] == '*': #down
                    #print("down.i=",i," j=",j)
                    mine += 1
            matrix[i][j] = str(mine)
for i in range(col):
    for j in range(row):
        print(matrix[i][j], end='')
    print()
