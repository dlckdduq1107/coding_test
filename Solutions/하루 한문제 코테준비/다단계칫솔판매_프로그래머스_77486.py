import math


def solution(enroll, referral, seller, amount):
    answer = []
    graph = {"-":[]}
    benefits = {}
    for i in range(len(enroll)):
        child,parent = enroll[i],referral[i]
        benefits[child] = 0;
        if(child not in graph):
            graph[child] = []
        graph[child]=parent

    for idx,person in enumerate(seller):
        money = amount[idx]*100
        me,pa = person,graph[person]
        while(pa != []):

            mine = math.ceil(money*0.9)
            sendMoney = money-mine
            if(sendMoney < 1):
                mine = money
                sendMoney = 0
                benefits[me] += mine
                me,pa = pa,graph[pa]
                money = sendMoney
                break

            benefits[me] += mine
            # benefits[pa] += sendMoney
            me,pa = pa,graph[pa]
            money = sendMoney
        #     print(me,pa,money,benefits)
        # print()



    for p in enroll:
        answer.append(benefits[p])
    # print(graph)
    # print(benefits)
    return answer


print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],["young", "john", "tod", "emily", "mary"],[12, 4, 2, 5, 10]))