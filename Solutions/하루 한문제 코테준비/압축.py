def solution(msg):
    answer = []
    dictionary = {}
    pivot = 1
    last = 27
    for i in range(1,27):
        dictionary[chr(64+i)] = i
    
    w,c = 0,0
    while True:
        c+=1
        if(c==len(msg)):
            answer.append(dictionary[msg[w:c+1]])
            break
        if(msg[w:c+1] not in dictionary):
            dictionary[msg[w:c+1]] = len(dictionary)+1
            answer.append(dictionary[msg[w:c]])
            w = c

    # print(dictionary)
    return answer
print(solution("TOBEORNOTTOBEORTOBEORNOT"))