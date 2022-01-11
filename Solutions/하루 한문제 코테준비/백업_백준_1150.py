n,k = map(int,input().split(" "))

distance = []
for i in range(n):
    distance.append(int(input()))

visited = [False for i in range(n)]
result = 0
while(k>0):
    pre = 0
    temp = int(1e9)
    start = 0
    end = 1
    for i in range(1,n):
        if(visited[i]):
            continue
        if(abs(distance[pre]-distance[i])<temp):
            temp = abs(distance[pre]-distance[i])
            start = pre
            end = i
        pre+=1
    visited[start],visited[end] = True,True
    result += temp
    k-=1
    print(visited,temp,start,end)

print(result)