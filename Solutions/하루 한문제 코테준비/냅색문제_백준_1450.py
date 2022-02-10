import bisect
def dfs(origin,sum_arr,count,value):
    if(count>=len(origin)):
        sum_arr.append(value)
        return
    dfs(origin,sum_arr,count+1,value)
    dfs(origin,sum_arr,count+1,value+origin[count])

n,c = map(int,input().split())
weight = list(map(int,input().split()))

fw,sw = weight[:len(weight)//2],weight[len(weight)//2:]
first,second = [],[]
dfs(fw,first,0,0)
dfs(sw,second,0,0)

# print(first,second)
second.sort()
result = 0
for i in first:
    # print(bisect.bisect_right(second,c-i),i)
    if(c-i<0):
        continue
    result += bisect.bisect_right(second,c-i)

print(result)