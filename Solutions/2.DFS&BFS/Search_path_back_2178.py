from collections import deque

def bfs(x,y): # bfs
    queue = deque() # 큐
    queue.append((x,y))

    while queue:# 큐가 빌때 까지
        x,y = queue.popleft()

        for i in range(4): # 4방향 탐색
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<= nx <row and 0<= ny <col: # 볌위안에 있을때
                if matrix[nx][ny] == 1:
                    matrix[nx][ny] = matrix[x][y] +1
                    queue.append((nx,ny))


row, col = map(int, input().split(" "))
matrix = []

dx = [0,0,1,-1]
dy = [1,-1,0,0]

for i in range(row): # 입력된 값 리스트로 변환하여 업데이트
    matrix.append(list(map(int,input())))

bfs(0,0) # bfs실행

print(matrix[row-1][col-1])
