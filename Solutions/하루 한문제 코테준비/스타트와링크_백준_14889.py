from itertools import combinations
def calNum():
    team1,team2 = 0,0
    t1,t2 = [],[]
    for idx,isTrue in enumerate(visited):
        if isTrue:
            t1.append(idx)
        else:
            t2.append(idx)
    for i,j in list(combinations(t1,2)):
        team1 += graph[i][j]+graph[j][i]
    for i,j in list(combinations(t2,2)):
        team2 += graph[i][j]+graph[j][i]
    return abs(team1-team2)

def dfs(start,count):
    global result
    if(count == n/2):
        result = min(result,calNum())
    else:
        for i in range(start,n):
            visited[i] = True
            dfs(i+1, count+1)
            visited[i] = False



n = int(input())
graph = []
visited = [False for i in range(n)]
result = int(1e9)
for i in range(n):
    graph.append(list(map(int,input().split(" "))))

dfs(0,0)
print(result)