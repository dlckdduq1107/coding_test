from curses import noecho
from optparse import Option
import re
def solution(dartResult):
    answer = 0
    result = []
    p = re.compile('[0-9]+[S|D|T][*|#]?')
    each_list = p.findall(dartResult)
    for idx,i in enumerate(each_list):
        # print(i)
        each = list(i)
        if(each[1]=='0'):
            score = 10
            square = each[2]
            if(len(each)==4):
                option = each[3]
            else:
                option = None
        else:
            score = int(each[0])
            square = each[1]
            if(len(each)==3):
                option = each[2]
            else:
                option = None

        if(square=='S'):
            result.append(score)
        elif(square=='D'):
            result.append(score**2)
        else:
            result.append(score**3)
        
        if(option is not None):
            if(option=='*'):
                result[idx] = result[idx]*2
                if(idx!=0):
                    result[idx-1] = result[idx-1]*2
            else:
                result[idx] = result[idx]*-1
        # print(result)
    return sum(result)

print(solution("1D2S#10S"))