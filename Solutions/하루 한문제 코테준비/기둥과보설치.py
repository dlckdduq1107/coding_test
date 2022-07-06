def check(gidung,x,y,graph,n):
    if(gidung==0):
        if(x==0 or (y-1>=0 and graph[x][y-1][1]==1) or (x-1>=0 and graph[x-1][y][0]==1)):
            return True
        return False
    else:
        if((x-1>=0 and graph[x-1][y][0]==1) or (y+1<=n and x-1>=0 and graph[x-1][y+1][0]==1) or ((y-1>=0 and graph[x][y-1][1]==1) and (y+1<=n and graph[x][y+1][1]==1))):
            return True
        return False

def solution(n, build_frame):
    answer = []
    graph = [[[0,0] for i in range(n+1)] for j in range(n+1)] # 기둥,보
    # for i in graph:
    #     print(*i)
    for y,x,t,build in build_frame:
        if(build): # 설치
            if(t==0):#기둥
                if(x==0 or (y-1>=0 and graph[x][y-1][1]==1) or (x-1>=0 and graph[x-1][y][0]==1)):
                    graph[x][y][0] = 1
            else:
                if((x-1>=0 and graph[x-1][y][0]==1) or (y+1<=n and x-1>=0 and graph[x-1][y+1][0]==1) or ((y-1>=0 and graph[x][y-1][1]==1) and (y+1<=n and graph[x][y+1][1]==1))):
                    graph[x][y][1] = 1
        else: # 삭제
            if(t==0):
                graph[x][y][0] = 0
                if(check(1,x+1,y-1,graph,n) and check(0,x+1,y,graph,n) and check(1,x+1,y,graph,n)):
                    pass
                else:
                    graph[x][y][0] = 1
            else:
                graph[x][y][1] = 0
                if(check(1,x,y-1,graph,n) and check(1,x,y+1,graph,n) and check(0,x,y+1,graph,n)):
                    pass
                else:
                    graph[x][y][1] = 1
        # for i in range(n,-1,-1):
        #     print(*graph[i])
        # print('\n\n\n\n')
    # for i in range(n,-1,-1):
    #     print(*graph[i])
    for idx,i in enumerate(graph):
        for idxj, j in enumerate(i):
            if(sum(j)==1):
                answer.append([idxj,idx,0 if j[0]==1 else 1])
    answer.sort(key=lambda x:x[2])
    answer.sort(key=lambda x:x[1])
    answer.sort(key=lambda x:x[0])
    return answer
print(solution(5,[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))