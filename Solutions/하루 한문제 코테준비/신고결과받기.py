from collections import defaultdict
def solution(id_list, report, k):
    answer = []
    attacked = defaultdict(set)
    for each in report:
        fromUser, toUser = each.split(' ')
        attacked[toUser].add(fromUser)
    # print(attacked)
    fromUserSet = defaultdict(int)
    for i in attacked.keys():
        eachAttacked = attacked[i]
        if(len(eachAttacked)>=k):
            for j in eachAttacked:
                fromUserSet[j] += 1
    # print(fromUserSet)
    for i in id_list:
        answer.append(fromUserSet[i])
    return answer

print(solution(["muzi", "frodo", "apeach", "neo"],["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))