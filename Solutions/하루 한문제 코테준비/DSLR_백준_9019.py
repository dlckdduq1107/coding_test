from collections import deque
def bfs(count,value,targetA,targetB):
    global limit
    q = deque([])
    q.append([count,value,targetA])

    visited = set()
    visited.add(targetA)
    while q:
        c,v,target = q.popleft()
        if(target==targetB):
            print(v)
            return

        # if(c<limit):
        D = target*2
        if(D>9999):
            D %= 10000
        if(D not in visited):
            visited.add(D)
            q.append([c+1,v+'D',D])

        S = target-1
        if(target==0):
            S=9999
        if(S not in visited):
            visited.add(S)
            q.append([c+1,v+'S',S])

        L = (target%1000)*10 + (target//1000)
        if(L not in visited):
            visited.add(L)
            q.append([c+1,v+'L',L])

        R = (target%10)*1000 + (target//10)
        if(R not in visited):
            visited.add(R)
            q.append([c+1,v+'R',R])


n = int(input())

for i in range(n):
    a,b = map(int,input().split())
    limit = int(1e9)

    bfs(0,'',a,b)