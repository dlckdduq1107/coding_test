from bisect import bisect_left

n = int(input())
n_list = list(map(int,input().split(" ")))
m = int(input())
m_list = list(map(int,input().split(" ")))

result = []
n_list.sort()

for i in m_list:
    res = bisect_left(n_list,i)
    if(res>=len(n_list) or n_list[res] != i):
        result.append(0)
    else:
        result.append(1)
    # if(i in n_list):
    #     result.append(1)
    # else:
    #     result.append(0)

print(*result)