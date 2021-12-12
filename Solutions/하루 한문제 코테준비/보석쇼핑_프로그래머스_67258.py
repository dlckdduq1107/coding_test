def solution(gems):
    length = len(set(gems))
    dic = {gems[0]:1}
    start,end = 0,0
    result = [0,len(gems)-1]
    while start < len(gems) and end <len(gems):
        if(len(dic)==length):
            if(end-start < result[1]-result[0]):
                result = [start,end]
            if(dic[gems[start]]==1):
                del dic[gems[start]]
            else:
                dic[gems[start]] -= 1
            start += 1

        else:
            end += 1
            if(end == len(gems)):
                break
            if(gems[end] in dic):
                dic[gems[end]] += 1
            else:
                dic[gems[end]] = 1

    return [result[0]+1,result[1]+1]

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["AA", "AB", "AC", "AA", "AC"]))
print(solution(["XYZ", "XYZ", "XYZ"]))
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))