def pre_dfs(start):
    print(chr(start+65),end='')
    if(graph[start][0]!=[]):
        pre_dfs(graph[start][0][0])
    if(graph[start][1]!=[]):
        pre_dfs(graph[start][1][0])

def in_dfs(start):

    if(graph[start][0]!=[]):
        in_dfs(graph[start][0][0])
    print(chr(start+65),end='')
    if(graph[start][1]!=[]):
        in_dfs(graph[start][1][0])

def post_dfs(start):

    if(graph[start][0]!=[]):
        post_dfs(graph[start][0][0])

    if(graph[start][1]!=[]):
        post_dfs(graph[start][1][0])
    print(chr(start+65),end='')

n = int(input())

graph = [[[],[]] for i in range(n+1)]
for i in range(n):
    a,b,c = map(ord,input().split())
    a,b,c = a-65,b-65,c-65
    if(b!=-19):
        graph[a][0].append(b)
    if(c!=-19):
        graph[a][1].append(c)

pre,in_order,post = [],[],[]

pre_dfs(0)
print()
in_dfs(0)
print()
post_dfs(0)