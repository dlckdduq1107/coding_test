import copy
from itertools import permutations
def check():
    for current in range(1,n+1):
        cur_flog = flog[current]
        if(not(current in like[cur_flog])):
            return False
        for next, subject in graph[current]:
            cur =interest[cur_flog][subject]
            nf = interest[next][subject]
            if(cur!=nf):
                return False
    return True

def dfs(start,count):
    global c
    if(count == n):
        #print(flog)
        if check():
            temp = copy.deepcopy(flog)

            result.append(temp)
    else:
        print(flog)
        for j in range(start,n+1): # 연꽃 번호
            if(flog[j] == 0):
                for i in range(start,n+1):#개구리 번호

                #print(i,j)

                    flog[j] = i
                    dfs(i+1,count+1)
                    flog[j] = 0
                    c+=1
"""
def temp():
    for i in list(permutations([i for i in range(1,n+1)],n)):
        w = [0]+list(i)
        if(check(w)):
            result.append(w)
"""
c=0
result = []
n,m = map(int, input().split(" "))
flog = [0 for i in range(n+1)]
interest = [[]]
for i in range(n):
    interest.append(list(map(int,[0]+input().split(" "))))

like = [[]]
for i in range(n):
    like.append(list(map(int,input().split(" "))))

graph = [[] for i in range(n+1)]
for i in range(m):
    a,b,t = map(int,input().split(" "))
    graph[a].append([b,t])
    #graph[b].append([a,t])

dfs(1,0)
#temp()
if(len(result) == 0):
    print("NO")
else:
    print("YES")
    res = result[0]
    res.pop(0)
    for i in res:
        print(i,end=" ")
print(c)
#print(result)