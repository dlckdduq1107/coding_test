from itertools import permutations
import copy
def solution(expression):
    answer = 0
    oper = set()
    temp = ''
    splitEx = []
    for i in expression:
        if(i=='-' or i=='+' or i=='*'):
            splitEx.append(temp)
            splitEx.append(i)
            oper.add(i)
            temp = ''
            continue
        temp += i
    splitEx.append(temp)

    result = 0
    for each in list(permutations(oper,len(oper))):
        # print(each)
        tempSplit = copy.deepcopy(splitEx)
        for operation in each:
            for idx,ex in enumerate(splitEx):
                if(ex==operation):
                    preIdx, postIdx = idx-1,idx+1
                    while tempSplit[preIdx] == '':
                        preIdx -=1
                    while tempSplit[postIdx] == '':
                        postIdx +=1
                    tempSplit[idx] = str(eval(tempSplit[preIdx]+ex+tempSplit[postIdx]))
                    tempSplit[preIdx],tempSplit[postIdx] = '',''
                    # print(tempSplit)

        result = max(result,abs(int(''.join(tempSplit))))
        # print(result)

    return result

print(solution("100-200*300-500+20"	))