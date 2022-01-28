def dfs(start):
    if(len(arr)==m):
        print(' '.join(list(map(str,arr))))
        return
    else:
        for i in range(start,n+1):
            arr.append(i)
            dfs(i)
            arr.pop()

n,m = map(int,input().split(" "))
arr = []
dfs(1)