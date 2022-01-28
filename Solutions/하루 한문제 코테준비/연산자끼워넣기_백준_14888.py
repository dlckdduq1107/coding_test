def dfs(value,count,plus,minus,mul,divide):
    global max_num,min_num
    if(count==n):
        max_num = max(max_num,value)
        min_num = min(min_num,value)
    else:
        if(plus>0):
            dfs(value+number[count],count+1,plus-1,minus,mul,divide)
        if(minus>0):
            dfs(value-number[count],count+1,plus,minus-1,mul,divide)
        if(mul>0):
            dfs(value*number[count],count+1,plus,minus,mul-1,divide)
        if(divide>0):
            dfs(int(value/number[count]),count+1,plus,minus,mul,divide-1)

n = int(input())
number = list(map(int,input().split(" ")))
oper = list(map(int,input().split(" ")))


max_num = int(-1e9)
min_num = int(1e9)
dfs(number[0],1,oper[0],oper[1],oper[2],oper[3])
print(max_num)
print(min_num)