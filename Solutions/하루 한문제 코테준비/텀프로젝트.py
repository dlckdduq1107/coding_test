import sys
sys.setrecursionlimit(111111)
def dfs(start):
    global result
    visited[start] = True
    num = graph[start]
    cycle.append(start)
    if(visited[num]):
        if(num in cycle):
            result.extend(cycle[cycle.index(num):])
    else:
        dfs(num)
n = int(input())
for i in range(n):
    people = int(input())
    graph = [0]
    graph.extend(list(map(int,input().split(' '))))
    visited = [True]+[False for j in range(people)]
    result = []
    for j in range(1,people+1):
        if(not visited[j]):
            cycle = []
            dfs(j)
    # print(result)
    print(people-len(result))
