from collections import deque

def bfs(x,y):
    queue = deque()
    queue.append((x,y)) # 시작구간 설정

    while queue:
        x,y = queue.popleft()

        # 클립보드에 복사
        if matrix[x][x] == 0: # 현재화면=클립보드의 노드가 아직 방문하지 않았으면
            matrix[x][x] = matrix[x][y]+1 # 현재값 +1
            queue.append((x,x)) # 큐 추가
         # 붙여넣기
        if x+y < n+1 and matrix[x+y][y] == 0: # 붙여넣기 한 값이 도착값넘지 않고 수정되지 않았으면
            matrix[x+y][y] = matrix[x][y]+1
            queue.append((x+y, y))
         # 한개 삭제
        if x-1 >= 0 and matrix[x-1][y] == 0: # 한개 삭제한 값이 0보다 작지 않고 수정되지 않았으면
            matrix[x-1][y] = matrix[x][y]+1
            queue.append((x-1, y))

n = int(input())
matrix = [[0 for j in range(1001)] for i in range(1001)] # [현재화면의 이모티콘수, 클립보드의 이모티콘수]

bfs(1,0) # 시작은 현재화면에 1개 이모티콘에 클립보드에 0개

res = int(1e9)
for i in matrix[n]: # 구하려는 노드에 도달하는 클립보드 중에서 가장작은거 출력
    if i != 0 and i < res:
        res = i

print(res)