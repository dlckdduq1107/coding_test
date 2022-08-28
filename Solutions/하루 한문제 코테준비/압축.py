def solution(msg):
    answer = []
    dictionary = {}
    pivot = 1
    last = 27
    for i in range(1,27):
        dictionary[chr(64+i)] = i
    
    i = 0
    while(i<len(msg)):#글자 반복
        for j in range(pivot,0,-1):#글자수 맞을때까지 반복
            if(i+j>len(msg)):
                continue
            each = msg[i:i+j]
            print(each,j)
            if(each in dictionary):
                answer.append(dictionary[each])
                if(i+j<len(msg)):
                    dictionary[each+msg[i+j]] = last
                last +=1
                i += j
                pivot = j+1
                break
        

    print(dictionary)
    return answer
print(solution("TOBEORNOTTOBEORTOBEORNOT"))