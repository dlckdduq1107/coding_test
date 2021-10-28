import copy
from collections import deque
#bfs할떄 처음 start에 True표시하고 연결된 노드가 visited Falsle이면 큐에 추가하고 True로 바꿔야한다.
#while문 안에서 현재노드를 True하면 이미들어간 노드가 True가 되지 않아 중복으로 들어간다.
def bfs(sx,sy,graph):
    q = deque([(sx,sy)])
    graph[sx][sy] = 0
    while(q):
        x,y = q.popleft()

        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if(0<=nx<n and 0<=ny<m and graph[nx][ny]!=0):
                q.append((nx,ny))
                graph[nx][ny] = 0
    return graph

n,m = map(int,input().split(" "))
graph = []
dx,dy = [0,0,1,-1],[1,-1,0,0]
for i in range(n):
    graph.append(list(map(int,input().split(" "))))

flag = True
result = 0
while(flag):
    result+=1
    temp = deque([])
    for i in range(1,n-1):
        for j in range(m):
            if(0<=i<n and 0<=j<m and graph[i][j]!=0):
                count = 0
                for q in range(4):
                    nx,ny = i+dx[q],j+dy[q]
                    if(graph[nx][ny]==0):
                        count+=1
                temp.append([i,j,count])

    tt = deque([])
    for x,y,num in temp:
        origin = graph[x][y]
        if(origin-num<=0):
            graph[x][y] = 0
            # tt.remove([x,y,num])
        else:
            tt.append([x,y,num])
            graph[x][y] -= num
    if(len(tt)==0):
        result=0
        break
    xx,yy,na = tt[0]
    tg = copy.deepcopy(graph)
    second = bfs(xx,yy,tg)
    total = sum([sum(q) for q in second])
    if(total != 0):
        flag = False
                #카운트세서 temp에 추가 한다음(x,y,숫자) temp안에 있는거 반복하면서 graph에 반영하고 bfs로 찾기 한번 더 찾아지면 break, 안나눠지는 경우는 생각해야됨

print(result)