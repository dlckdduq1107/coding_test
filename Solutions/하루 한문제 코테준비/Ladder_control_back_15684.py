
def sameCheck():
    for i in range(n):
        start = i
        tempj = 0
        for j in range(h):
            if(start<n-1 and checked[j][start]):
                start += 1
            elif(start >0 and checked[j][start-1]):
                start -= 1

        if(start!=i):
            return False

    return True

def dfs(sx,se, count,target):
    global result,flag,a,b
    if(flag):
        return
    if(count==target):
        if(sameCheck()):
            result = min(count,result)
            flag = True
            return

    else:
        for i in range(sx,h):
            if i == sx: k = se # 행이 변경되기 전에는 가로선을 계속해서 탐색
            else: k = 0 # 행이 변경될 경우 가로선 처음부터 탐색
            for j in range(k,n-1):

                if(checked[i][j]):
                    continue
                if(j-1>=0 and checked[i][j-1]):
                    continue
                if(j+1<n-1 and checked[i][j+1]):
                    continue

                checked[i][j] = True
                dfs(i,j,count+1,target)
                checked[i][j] = False

result = int(1e9)
flag = False
n,m,h = map(int,input().split(" "))
if(m==0):
    print(0)
    exit(0)

checked = [[False for i in range(n-1)] for j in range(h)]
for i in range(m):
    a,b = map(int,input().split(" "))
    checked[a-1][b-1] = True
if(sameCheck()):
    print(0)
    exit(0)
for i in range(1,4):
    if(not flag):
        dfs(0,0,0,i)

if(result == int(1e9)):
    print(-1)
else:
    print(result)

