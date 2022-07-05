def check(gidung,x,y,graph):
    if(gidung==0):
        if(y==0 or (x-1>=0 and graph[x-1][y][1]==1) or (x+1<n and graph[x+1][y][1]==1) or (y-1>=0 and graph[x][y-1][0]==1)):
            return True
        return False
    else:
        if ((y-1>=0 and graph[x][y-1][0]==1) or (x+1<n and y-1>=0 and graph[x+1][y-1][0]==1) or (x-1>=0 and graph[x-1][y][1]==1) or (x+1<n and graph[x+1][y][1]==1)):
            return True
        return False

def solution(n, build_frame):
    answer = [[]]
    graph = [[[0,0] for i in range(n+1)] for j in range(n+1)]
    # for i in graph:
    #     print(*i)
    for y,x,t,build in build_frame:
        if(build): # 설치
            if(t==0):#기둥
                if(y==0 or (x-1>=0 and graph[x-1][y][1]==1) or (x+1<n and graph[x+1][y][1]==1) or (y-1>=0 and graph[x][y-1][0]==1)):
                    graph[x][y][0] = 1
            else:
                if((y-1>=0 and graph[x][y-1][0]==1) or (x+1<n and y-1>=0 and graph[x+1][y-1][0]==1) or (x-1>=0 and graph[x-1][y][1]==1) or (x+1<n and graph[x+1][y][1]==1)):
                    graph[x][y][1] = 1
        else: # 삭제
            if(t==0):
                if(check(0,x+1,y,graph) and check(0,x-1,y,graph) and check(1,x-1,y,graph) and check(1,x+1,y,graph) and check(1,x-1,y+1,graph) and check(1,x+1,y+1,graph)):
                    graph[x][y][0] = 0
            else:
                if(check(1,x-1,y,graph) and check(1,x+1,y,graph) and check(0,x,y-1,graph) and check(0,x,y+1,graph) and check(0,x+1,y+1,graph) and check(0,x+1,y-1,graph)):
                    graph[x][y][1] = 0
        for i in range(n,-1,-1):
            print(*graph[i])
        print('\n\n\n\n')
    # for i in range(n,-1,-1):
    #     print(*graph[i])
    return answer
print(solution(5,[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))