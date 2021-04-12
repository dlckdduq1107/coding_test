def two_even():
    find_min = min(map(min,matrix))
    for i in range(r):
        for j in range(c):
            if matrix[i][j] == find_min:
                min_row = i
                min_col = j

    #print(min_row,min_col)
    a_list = []
    a_row, a_col = 0,0
    b_list = []
    b_row, b_col = r-1, c-1

    while a_row+2 <= min_row:
        a_list.append("R"*(c-1))
        a_list.append("D")
        a_list.append("L" * (c-1))
        a_list.append("D")
        a_row += 2

    while b_row-2 >= min_row:
        b_list.append("R"*(c-1))
        b_list.append("D")
        b_list.append("L" * (c-1))
        b_list.append("D")
        b_row -= 2

    mul_row = b_row-a_row+1
    while a_col+2 <= min_col:
        a_list.append("D"*(mul_row-1))
        a_list.append("R")
        a_list.append("U" * (mul_row-1))
        a_list.append("R")
        a_col += 2

    while b_col-2 >= min_col:
        b_list.append("D"*(mul_row-1))
        b_list.append("R")
        b_list.append("U" * (mul_row-1))
        b_list.append("R")
        b_col -= 2

    if a_col == min_col:
        a_list.append("RD")
    else:
        a_list.append("DR")

    b_list.reverse()

    result = a_list+b_list
    for data in result:
        print(data,end="")


def one_even_one_odd():
    for i in range(r//2):
        print("R"*(c-1),end="")
        print("D", end="")
        print("L" * (c - 1), end="")
        print("D", end="")
    print("R"*(c-1),end="")
def two_odd():
    for i in range(c//2):
        print("D"*(r-1),end="")
        print("R", end="")
        print("U" * (r - 1), end="")
        print("R", end="")
    print("D"*(r-1),end="")





r,c = map(int, input().split()) # 입력
matrix = []

for i in range(r): # a매트릭스 입력
    q = list(map(int,input().split(" ")))
    matrix.append(q)

if c%2 == 1:
    two_odd()
elif r%2 == 1:
    one_even_one_odd()
elif r%2 == 0 and c%2 == 0:
    two_even()


