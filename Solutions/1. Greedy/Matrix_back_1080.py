def flip(i,j,mat): # 3X3 뒤집기
    i -= 1
    j -= 1
    for q in range(3):
        for w in range(3):
            mat[i][j] = abs(mat[i][j]-1)
            j += 1
        j -= 3
        i += 1
    return mat


n,m = map(int, input().split()) # 입력
matrix_a = []
matrix_b = []

for i in range(n): # a매트릭스 입력
    q = list(map(int,list(input())))
    matrix_a.append(q)

for i in range(n): # b매트릭스 입력
    q = list(map(int,list(input())))
    matrix_b.append(q)

count = 0
for pivot_row in range(n-2): # 피벗 행-2 반복
    for pivot_col in range(m-2): # 피벗 열-2 반복
        if matrix_a[pivot_row][pivot_col] != matrix_b[pivot_row][pivot_col]: # 요소가 다르면 뒤집기
            matrix_a = flip(pivot_row+1, pivot_col+1,matrix_a)
            count += 1

if matrix_a != matrix_b: # 다르면
    print(-1)
else: #같으면
    print(count)




