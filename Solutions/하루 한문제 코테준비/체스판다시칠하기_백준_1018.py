def check(x,y,graph):
    c1,c2 = 0,0
    for i in range(x,x+8):
        for j in range(y,y+8):
            if((i+j)%2==0):
                if(graph[i][j]=='W'):
                    c2 += 1
                if(graph[i][j]=='B'):
                    c1 += 1
            else:
                if(graph[i][j]=='B'):
                    c2 += 1
                if(graph[i][j]=='W'):
                    c1 += 1
    print(c1,c2)
    return min(c2,c2)

n,m = map(int,input().split(' '))

graph = []
for i in range(n):
    graph.append(list(input()))

result = int(1e9)
for i in range(n-7):
    for j in range(m-7):
        result = min(check(i,j,graph),result)
        print(result)

print(result)