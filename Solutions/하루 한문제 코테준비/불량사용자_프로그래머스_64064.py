import copy
import re
from itertools import permutations
def check(origin,patterns):
    for idx,i in enumerate(patterns):
        p = re.compile(i)
        m = p.match(origin[idx])
        if(not m):
            return False
        if(m.group() != origin[idx]):
            return False
        # print(i,origin[idx],p.match(origin[idx]))
    return True



def solution(user_id, banned_id):
    answer = 0
    pattens = []
    for patten in banned_id:
        temp = ''
        for each in patten:
            if(each =='*'):
                temp += "[0-9a-z]"
            else:
                temp += each
        pattens.append(temp)
    # print(pattens)
    userList = permutations(user_id,len(pattens))
    # print(userList)
    result = []
    for i in userList:
        if(check(list(i),pattens)):
            if(set(i) not in result):
                result.append(set(i))
            # print(set(i),pattens)
    # print(result)
    return len(result)

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "abc1**"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["*rodo", "*rodo", "******"]))