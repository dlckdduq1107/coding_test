# 1 1 2   3       6   7   30
# 1 2 3,4 4,5,6,7 7,8,9,10,

n = int(input())
num_list = list(map(int,input().split(" ")))
num_list.sort()
result = 1
if(1 not in num_list):
    print(result)
    exit(0)
start,end = 0,num_list.pop(0)
for i in num_list:
    next_start, next_end = start+i, end+i
    if(next_start<=end):
        end = next_end
    else:
        result = end + 1

print(result)