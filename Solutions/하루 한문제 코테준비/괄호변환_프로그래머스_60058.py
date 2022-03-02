def check(string):
    temp = {')':'('}
    stack = []
    for i in string:
        if(i not in temp):
            stack.append(i)
        else:
            if(not stack or temp[i] != stack.pop()):
                return False
    return len(stack)==0

def solution(p):
    answer = ''
    return answer

print(solution("()))((()"))