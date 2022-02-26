def rotate(arr):

    return arr
def solution(rows, columns, queries):
    answer = []
    arr = [[i for i in range(j*columns+1,j*columns+columns+1)] for j in range(rows)]
    print(arr)
    return answer

print(solution(6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]]))