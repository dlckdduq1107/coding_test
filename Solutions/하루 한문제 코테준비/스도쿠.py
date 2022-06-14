def check(x,y,target):
    for i in range(9):
        if(target==arr[i][y]): return False
        if(target==arr[x][i]): return False
    sx,sy = (x//3)*3,(y//3)*3
    for i in range(sx,sx+3):
        for j in range(sy,sy+3):
            if(arr[i][j]==target): return False
    return True

def dfs(count):
    if(count==len(zeros)):
        for i in arr:
            print(' '.join(list(map(str,i))))
        return
    else:
        for i in range(1,10):
            x,y = zeros[count]
            if(check(x,y,i)):
                arr[x][y] = i
                dfs(count+1)
                arr[x][y] = 0

arr = []
zeros = []
for i in range(9):
    temp = list(map(int, input().split(' ')))
    for j,value in enumerate(temp):
        if(value==0):
            zeros.append((i,j))
    arr.append(temp)

dfs(0)