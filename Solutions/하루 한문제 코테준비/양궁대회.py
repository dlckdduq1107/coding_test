import copy
def cal_num(lion,apeach):
    lion_total,apeach_total = 0,0
    for i in range(11):
        l,a = lion[i], apeach[i]
        if(l+a==0):
            continue
        if(l>a):
            lion_total += 10-i
        else:
            apeach_total += 10-i
    return lion_total-apeach_total

def dfs(lion_list,count,idx,info,n):
    global differ,answer
    if(idx>10):
        return
    if(count==n):
        temp = cal_num(lion_list, info)
        if(temp>0):
            if(differ<=temp):
                if(temp==differ):
                    for i in range(10,-1,-1):
                        if(lion_list[i]>answer[i]):
                            answer = copy.deepcopy(lion_list)
                            break
                        if(lion_list[i]<answer[i]):
                            break
                else:
                    answer = copy.deepcopy(lion_list)
                    differ = temp
    else:
        lion_list[idx] += 1
        dfs(lion_list,count+1,idx,info,n)
        lion_list[idx] -= 1

        dfs(lion_list,count,idx+1,info,n)
def solution(n, info):
    global differ,answer
    arr = [0 for i in range(11)]
    differ = int(-1e9)
    dfs(arr,0,0,info,n)
    if(differ==int(-1e9)):
        answer = [-1]
    return answer
