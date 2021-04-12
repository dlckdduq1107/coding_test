from collections import deque

def bfs(location):

    queue = deque()
    for i,j in location: # 큐에 1의 위치를 먼저 넣어주면 차례대로 퍼져나간다.
        queue.append((i,j))

    while queue: # 큐 구현
        x,y = queue.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<= nx < row and 0<= ny < col:
                if matrix[nx][ny] == 0 :
                    matrix[nx][ny] = matrix[x][y] + 1
                    queue.append((nx,ny))


col,row = map(int, input().split(" "))
matrix = []
dx = [0,0,1,-1]
dy = [1,-1,0,0]
location = [] # 1의 위치 리스트

for i in range(row): # 입력에 대한 배열 구성
    matrix.append(list(map(int, input().split(" "))))

for i in range(len(matrix)): # 1이 들어간 위치를 리스트에 넣어줌
    for j in range(len(matrix[i])):
        if matrix[i][j] == 1:
            location.append([i,j])

bfs(location)

if any(0 in i for i in matrix): # 0이 존재하면
    print(-1)
else: # 아니면
    print(max(map(max, matrix))-1)