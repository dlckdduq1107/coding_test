def dfs(plus,minus,multi,div,value,count):
    global res_max,res_min
    if(n==count):
        res_max = max(res_max, value)
        res_min = min(res_min, value)
    else:
        if(plus>0):
            dfs(plus-1,minus,multi,div,value+numbers[count], count+1)
        if(minus>0):
            dfs(plus,minus-1,multi,div,value-numbers[count], count+1)
        if(multi>0):
            dfs(plus,minus,multi-1,div,value*numbers[count], count+1)
        if(div>0):
            dfs(plus,minus,multi,div-1,int(value/numbers[count]), count+1)




n = int(input())
numbers = list(map(int,input().split(' ')))
plus,minus,multi,div = map(int,input().split(' '))
res_min = int(1e9)
res_max = int(-1e9)

dfs(plus,minus,multi,div,numbers[0],1)

print(res_max)
print(res_min)