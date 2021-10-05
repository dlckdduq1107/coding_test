def solution(s):
    answer = int(1e9)
    for i in range(1,len(s)//2+1):
        result = ""
        temp=1
        pre = s[0:i]
        for j in range(i,len(s)+i,i):
            part = s[j:j+i]
            # print(pre,part,i,j)
            if(pre==part):
                temp+=1
            else:
                if(temp==1):
                    result += pre
                else:
                    result += str(temp)+pre

                pre = s[j:j+i]
                temp = 1
            # if(j==len(s)//i+i):

        # print(result)
        answer = min(answer,len(result))




    return min(answer,len(s))

print(solution("aabbaccc"))
# print(solution("ababcdcdababcdcd"))
# print(solution("abcabcdede"	))
# print(solution("abcabcabcabcdededededede"	))
