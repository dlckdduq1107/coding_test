def empty(x,y,target):
    for i in range(9):
       if(target==graph[x][i]):
           return False
       if(target==graph[i][y]):
            return False


    startX,startY = (x//3)*3,(y//3)*3
    for i in range(startX,startX+3):
        for j in range(startY,startY+3):
            if(target==graph[i][j]):
                return False

    return True

def dfs(count):
    if(count==len(zero_count)):
        for i in graph:
            print(' '.join(list(map(str,i))))
        exit(0)
    else:
        for i in range(1,10):
            x,y = zero_count[count]
            if(empty(x,y,i)):
                graph[x][y] = i
                dfs(count+1)
                graph[x][y] = 0
graph = []
zero_count = []
for i in range(9):
    row = list(map(int,input().split(" ")))
    for j,val in enumerate(row):
        if(val==0):
            zero_count.append((i,j))
    graph.append(row)

# print(zero_count)
dfs(0)

