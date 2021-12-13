import copy
from collections import deque
dx,dy = [0,0,1,-1],[1,-1,0,0]
def bfs(sx,sy):
    q = deque()
    q.append((sx,sy,0,0))

    while q:
        x,y,direction,value = q.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if(0<=nx<n and 0<=ny<n):
                if(cpyBoard[nx][ny]==0):
                    if(x==0 and y==0):
                        newValue = value+100
                    else:
                        if(direction==i):
                            newValue = value+100
                        else:
                            newValue = value+600

                    if(cost[nx][ny]>=newValue):
                        cost[nx][ny] = newValue
                        q.append((nx,ny,i,newValue))




def solution(board):
    global result,n,cost,cpyBoard
    cpyBoard = copy.deepcopy(board)
    n = len(board)
    cost = [[int(1e9) for i in range(n)]for j in range(n)]
    answer = 0

    cost[0][0] = 0
    bfs(0,0)
    # for i in cost:
    #     print(i)
    return cost[-1][-1]

print(solution(	[[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0]]))