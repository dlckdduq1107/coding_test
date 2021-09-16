def cal():
    temp = 0
    for idx,i in enumerate(visited):
        if(i):
            temp+= plan[idx][1]

    return temp

def dfs(start, count,plus):
    global result

    if(count>=n):
        if(count ==n):
            result = max(result,cal())
        else:
            result = max(result,cal()-plan[count-plus][1])


    else:
        for i in range(count,n):
            visited[i]=True
            dfs(start,i+plan[i][0],plan[i][0])
            visited[i]=False

n = int(input())
plan = []
result = 0
visited = [False for i in range(n)]
for i in range(n):
    a,b = map(int, input().split(" "))
    plan.append([a,b])


dfs(0,0,0)
print(result)