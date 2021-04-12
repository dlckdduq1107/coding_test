from collections import deque
#####x,y,z위치 바뀌는거 주의#######

def bfs(location): # 3차원 bfs
    queue = deque()
    for i,j,w in location:
        queue.append((i,j,w))

    while queue:
        x, y, z = queue.popleft()
        for i in range(6): # 6방향 x,y,z방향 바뀜
            nx = x+dx[i]
            ny = y+dy[i]
            nz = z+dz[i]

            if 0<= nx < height and 0<= ny < row and 0<= nz < col: # 범위 안벗어나게
                if matrix[nx][ny][nz] == 0:
                    matrix[nx][ny][nz] = matrix[x][y][z] + 1
                    queue.append((nx,ny,nz))


col, row, height = map(int,input().split(" "))
dx = [0,0,1,-1,0,0]
dy = [1,-1,0,0,0,0]
dz = [0,0,0,0,1,-1]
matrix = []
m = []
location = []

for i in range(height): # 입력을 3차원리스트로 변환
    for j in range(row):
        m.append(list(map(int, input().split(" "))))
    matrix.append(m)
    m = []

for i in range(height): # 1의 위치 파악
    for j in range(row):
        for w in range(col):
            if matrix[i][j][w] == 1:
                location.append([i,j,w])

bfs(location)

z = 1
result = -1
for i in range(height):
    for j in range(row):
        for w in range(col):
            if matrix[i][j][w] == 0: # 0이 있을 경우 표시
                z = 0
            result = max(result,matrix[i][j][w]) # 각 요소마다 최댓값 저장

if z == 0:
    print(-1)
else:
    print(result-1)