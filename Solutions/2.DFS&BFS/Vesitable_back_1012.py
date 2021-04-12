from collections import deque

def bfs(x,y,total):
    if matrix[x][y] == 1: # 1이면 테스트케이스에 해당하는 카운트 +1
        total_num[total] += 1 # +1
        queue = deque()
        queue.append((x,y))

        while queue: # 큐가 없어질때 까지
            x,y = queue.popleft()

            for i in range(4): # 4방향탐색
                nx = x+dx[i]
                ny = y+dy[i]

                if 0<= nx <row and 0<=ny<col: # 범위안에 있으면
                    if matrix[nx][ny] == 1: # 탐색한 요소가 1이면
                        matrix[nx][ny] = matrix[x][y] + 1 # 전에꺼에 +1
                        queue.append((nx,ny)) # 다음탐색을 위해 append

def make_matrix(i,j): # 배열 0으로 초기화
    mat = [[0 for q in range(j)] for w in range(i)]
    return mat

case = int(input())
total_num = [0 for i in range(case)] # 테스트케이스 개수만큼의 요소 0 초기화
dx = [0,0,-1,1]
dy = [1,-1,0,0]

for i in range(case):# 테스트케이스 만큼 반복
    row,col,num = map(int,input().split(" "))
    matrix = make_matrix(row,col)

    for j in range(num): # 지정된 위치 1로 바꿔주기
        location_i,location_j = map(int, input().split(" "))
        matrix[location_i][location_j] = 1

    for r in range(row): # bfs실행
        for c in range(col):
            bfs(r,c,i)

for i in total_num:
    print(i)
print(matrix)


