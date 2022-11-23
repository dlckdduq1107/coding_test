from collections import defaultdict
def solution(survey, choices):
    answer = ''
    personality = defaultdict(int)
    each_personal = [['R','T'],['C','F'],['J','M'],['A','N']]

    for i in range(len(survey)):
        [disagree, agree] = list(survey[i])
        num = choices[i]

        if(4-num > 0):
            personality[disagree] += abs(4-num)
        else:
            personality[agree] += abs(4-num)

    for first,second in each_personal:
        if(personality[first]<personality[second]):
            answer += second
        else:
            answer += first
    return answer

print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))