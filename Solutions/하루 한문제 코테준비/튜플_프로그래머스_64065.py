import re
def solution(s):
    answer = []
    p = re.compile('{[0-9,]+}')
    # print(p.findall(s))
    part = p.findall(s)
    resultPart = []
    for i in part:
        resultPart.append(list(map(int,i[1:-1].split(','))))
    resultPart.sort(key=lambda x:len(x))
    # print(resultPart)
    result = []
    for i in resultPart:
        for j in i:
            result.append(j)
    # print(list(dict.fromkeys(result)))
    return list(dict.fromkeys(result))

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"	))