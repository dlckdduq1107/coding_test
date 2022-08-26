
import math


def sum_set(a,b):
    result = []
    temp_a = a.copy()
    temp_b = b.copy()
    for i in a:
        if(i in temp_b):
            temp_b.remove(i)
            result.append(i)
        else:
            result.append(i)
    for i in temp_b:
        result.append(i)
    return result
def sub_set(a,b):
    result = []
    temp_b = b.copy()
    for i in a:
        if(i in temp_b):
            result.append(i)
            temp_b.remove(i)
    return result

def solution(str1, str2):
    answer = 0
    s1,s2 = [],[]
    for i in range(len(str1)-1):
        each = (str1[i]+str1[i+1]).upper()
        if(each.isalpha()):
            s1.append(each)
    for i in range(len(str2)-1):
        each = (str2[i]+str2[i+1]).upper()
        if(each.isalpha()):
            s2.append(each)
    # print(s1,s2)
    if(len(s1)==0 or len(s2)==0):
        return 65536
    answer = len(sub_set(s1,s2))/len(sum_set(s1,s2))
    answer*=65536
    # print(sub_set([1,1,2,2,3],[1,2,2,4,5]))
    return math.floor(answer)
print(solution("aa1+aa2","AAAA12"))