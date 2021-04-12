import sys
from collections import deque
input = sys.stdin.readline

#n#bfs로 하면 시간초과뜸###
# # def bfs(sx,sy,px,py):
# #     queue = deque() # 시작 노드추가
# #     queue.append([sx,sy,px,py])
# #
# #     while queue: # 큐가 텅 빌때까지
# #         nx, ny, pre_x, pre_y = queue.popleft() # pop
# #         r,c = abs(nx-pre_x), abs(ny-pre_y)
# #
# #         if r == 0 and c == 1: # 가로
# #             now_x = nx
# #             now_y = ny+1
# #             if 0 <= now_x < n and 0 <= now_y < n and graph[now_x][now_y] != 1:
# #                 pre_graph[now_x][now_y].append((nx,ny))
# #                 queue.append([now_x, now_y, nx, ny])
# #
# #             now_x = nx + 1
# #             now_y = ny + 1
# #             if 0 <= now_x < n and 0 <= now_y < n and graph[now_x][now_y] != 1 and graph[now_x-1][now_y] != 1 and graph[now_x][now_y-1] != 1:
# #                 pre_graph[now_x][now_y].append((nx,ny))
# #                 queue.append([now_x, now_y, nx, ny])
# #
# #         elif r == 1 and c == 0: # 세로
# #             now_x = nx + 1
# #             now_y = ny
# #             if 0 <= now_x < n and 0 <= now_y < n and graph[now_x][now_y] != 1:
# #                 pre_graph[now_x][now_y].append((nx, ny))
# #                 queue.append([now_x, now_y, nx, ny])
# #
# #             now_x = nx + 1
# #             now_y = ny + 1
# #             if 0 <= now_x < n and 0 <= now_y < n and graph[now_x][now_y] != 1 and graph[now_x - 1][now_y] != 1 and \
# #                     graph[now_x][now_y - 1] != 1:
# #                 pre_graph[now_x][now_y].append((nx, ny))
# #                 queue.append([now_x, now_y, nx, ny])
# #
# #         elif r == 1 and c == 1: # 대각선
# #             for i in range(2):
# #                 now_x = nx + dia_dx[i]
# #                 now_y = ny + dia_dy[i]
# #                 if 0 <= now_x < n and 0 <= now_y < n and graph[now_x][now_y] != 1:
# #                     pre_graph[now_x][now_y].append((nx, ny))
# #                     queue.append([now_x, now_y, x, ny])
#
#             now_x = nx + 1
#             now_y = ny + 1
#             if 0 <= now_x < n and 0 <= now_y < n and graph[now_x][now_y] != 1 and graph[now_x - 1][now_y] != 1 and \
#                     graph[now_x][now_y - 1] != 1:
#                 pre_graph[now_x][now_y].append((nx, ny))
#                 queue.append([now_x, now_y, nx, ny])

def dfs(sx,sy,direct):
    global count
    if sx == n-1 and sy == n-1: # 마지막에 오면 +1
        count += 1
        return

    if direct == 0 or direct == 2: # 가로와 대각선의 경우 가로로 이동할 수 있다.
        if sy + 1 < n: # 범위안에 있어야함
            if graph[sx][sy+1] == 0: # 이동하는 곳이 0 이어야 함
                dfs(sx,sy+1,0) # 가로방향 재귀

    if direct == 1 or direct == 2: #세로와 대각선의 경우 세로로 이동할 수있다.
        if sx + 1 < n: # 범위안
            if graph[sx+1][sy] == 0: # 이동하는 곳이 0
                dfs(sx+1,sy,1) # 세로방향 재귀

    if direct == 0 or direct == 1 or direct == 2: # 세가지 경우 모두 대각선으로 이동할 수 있다.
        if sy + 1 < n and sx + 1 < n: # 범위안
            if graph[sx+1][sy+1] == 0 and graph[sx+1][sy] == 0 and graph[sx][sy+1] == 0: # 세칸 모두 0이어야 함
                dfs(sx+1,sy+1,2) # 대각선 방향 재귀

n = int(input())

graph = []
count = 0

##BFS
# row_dx = [0,1] # 가로방향 bfs
# row_dy = [1,1]
# col_dx = [1,1] # 세로방향 bfs
# col_dy = [0,1]
# dia_dx = [1,0,1] # 대각선 방향 bfs
# dia_dy = [0,1,1]

for i in range(n):
    a = list(map(int,input().split(" ")))
    graph.append(a)

##BFS
# pre_graph = [[[]for i in range(n)] for j in range(n)] # 각 노드로 어디서 왔는지 인덱스기록하는 배열
# x,y = 0,1

# bfs(x,y,0,0)


##DFS
dfs(0,1,0)
print(count)