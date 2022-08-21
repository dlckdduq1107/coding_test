# 1 1 2   3       6   7   30
# 1 2 3,4 4,5,6,7 7,8,9,10,

n = int(input())
num_list = list(map(int,input().split(" ")))
num_list.sort()
print(num_list)
collected_set = set()
flag = False
result = 0
for i in num_list:    
    for j in list(collected_set):
        collected_set.add(j+i)
        if(sum(collected_set) != ((len(collected_set))*(len(collected_set)+1))/2):
            result = len(collected_set)
            flag = True
            break
    if flag:
        break
    collected_set.add(i)
    print(collected_set)
print(result)