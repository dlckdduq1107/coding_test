from collections import deque

def bfs():
    queue = deque()
    queue.append((0,0,0)) # 0번째 줄에서는 안깬 상태의 거리 저장

    while queue:
        x,y,z = queue.popleft()
        if x == n-1 and y == m-1: # 도착지에 도달하면 바로 출력
            return visited[x][y][z] +1

        for i in range(4): # 4방향
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<= nx < n and 0<= ny < m: # 범위내에 있을때
                if matrix[nx][ny] == 0 and visited[nx][ny][z] == 0: # 다음이 막히지 않고, 다음이 가보지 않았던 길일때(벽깬 여부는 상관X)
                    visited[nx][ny][z] = visited[x][y][z] + 1 # 이전에서 +1
                    queue.append((nx,ny,z)) # 벽깬 여부와 같이 append
                if matrix[nx][ny] == 1 and z == 0: # 다음이 벽으로 막히고, 아직 벽을 안깼을때(0번째 줄에서 진행하고 있을때)
                    visited[nx][ny][1] = visited[x][y][0] + 1 # 0번째 줄에서 진행하던걸 1번째 줄로 옮겨줌
                    queue.append((nx,ny,1)) # 다음 부터는 1번째 줄로 진행
    return -1 # 큐가 다 돌아도 도착점을 찾지 못해 -1 리턴



n,m = map(int, input().split(" "))
matrix = []
dx = [0,0,1,-1]
dy = [1,-1,0,0]
visited = [[[0,0] for i in range(m)] for j in range(n)] # 거리와 벽 깬 여부의 길을 나눠주는 리스트

for i in range(n): # 배열 입력
    matrix.append(list(map(int,input())))


print(bfs())
