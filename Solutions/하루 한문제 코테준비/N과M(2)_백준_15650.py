def dfs():
    if(len(arr)==m):
        if(arr==sorted(arr)):
            print(' '.join(list(map(str,arr))))
    else:

        for i in range(1,n+1):
            if(i not in arr):
                arr.append(i)

                dfs()
                arr.pop()

n,m = map(int,input().split(" "))

arr = []
dfs()