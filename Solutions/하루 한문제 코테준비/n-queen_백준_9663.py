def check(pre_row):
    for i in range(pre_row):
        if(arr[pre_row]==arr[i] or pre_row-i==abs(arr[pre_row]-arr[i])):
            return False
    return True

def dfs(count):
    global result
    if(count==n):
        result+=1
    else:
        for i in range(n):
            arr[count] = i
            if(check(count)):
                dfs(count+1)
result = 0
n = int(input())
arr = [0 for i in range(n)]
dfs(0)
print(result)