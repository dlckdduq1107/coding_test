def solution(id_list, report, k):
    answer = []
    limit = {}
    gobal = {}
    for i in id_list:
        limit[i] = 0
        gobal[i] = []
    for i in report:
        attack, target = i.split(" ")
        if(target not in gobal[attack]):
            gobal[attack].append(target)
            limit[target] += 1
    
    for i in id_list:
        temp = 0
        for j in gobal[i]:
            if(limit[j]>=k):
                temp += 1
        answer.append(temp)
    return answer