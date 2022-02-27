def rotate(arr,sx,sy,ex,ey):
    temp = arr[sx][sy]
    min_value = temp
    for i in range(sx+1,ex+1):
        arr[i-1][sy] = arr[i][sy]
        min_value = min(min_value,arr[i][sy])
    for i in range(sy+1,ey+1):
        arr[ex][i-1] = arr[ex][i]
        min_value = min(min_value,arr[ex][i])
    for i in range(ex-1,sx-1,-1):
        arr[i+1][ey] = arr[i][ey]
        min_value = min(min_value,arr[i][ey])
    for i in range(ey-1,sy,-1):
        arr[sx][i+1] = arr[sx][i]
        min_value = min(min_value,arr[sx][i])
    arr[sx][sy+1] = temp
    return [arr,min_value]
def solution(rows, columns, queries):
    answer = []
    arr = [[i for i in range(j*columns+1,j*columns+columns+1)] for j in range(rows)]

    for sx,sy,ex,ey in  queries:
        [arr,m] = rotate(arr,sx-1,sy-1,ex-1,ey-1)
        answer.append(m)

    return answer

print(solution(6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]]))