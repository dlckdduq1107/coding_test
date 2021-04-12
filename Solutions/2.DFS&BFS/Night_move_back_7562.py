from collections import deque

def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x,y = queue.popleft()

        for i in range(8): # 8방향 탐색
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<= nx< length and 0<= ny < length: # 범위내에 있으면
                if matrix[nx][ny] == 0: # 아직 탐색하지 않은 곳이면
                    if x == ei and y == ej: # 시작과 끝이 같을때
                        pass
                    else:
                        matrix[nx][ny] = matrix[x][y] + 1
                        queue.append((nx,ny))
                # if matrix[nx][ny] >= matrix[x][y]: ####더 큰거 들어오는 문제는 0일때만 받아주면 해결됨
                #     matrix[nx][ny] = matrix[x][y] + 1
                #     queue.append((nx,ny))
    case_list.append(matrix[ei][ej]) # 테스트 케이스에 대한 결과 추가
    # print(matrix)

case_num = int(input())
case_list = []
dx = [2,2,1,1,-2,-2,-1,-1] # 8방향에 대한 리스트
dy = [-1,1,2,-2,1,-1,2,-2]

for _ in range(case_num): # 테스트 케이스 반복
    length = int(input()) # 체스판 크기
    matrix = [[0 for i in range(length)] for j in range(length)] # 체스판 배열
    si, sj = map(int,input().split(" "))
    ei,ej = map(int, input().split(" "))

    bfs(si,sj)


for i in  case_list:
    print(i)