
def divide(target): # 균형잡힌 괄호 나누기
    start,end = 0,0
    for idx,each in enumerate(target):
        if(each == '('):
            start += 1
        if(each==')'):
            end += 1
        if(start==end):
            return target[:idx+1], target[idx+1:]
def check(target):# 스택을 이용한 올바른 괄호 판단
    stack = []
    for i in target:
        if(i=='('):
            stack.append(i)
        else:
            if(not stack):
                return False
            stack.pop()
    return True
def dfs(target): # 요구사항 그대로 반영
    if(target==''):
        return ''
    u,v = divide(target)
    if(check(u)):
        return u+dfs(v)

    else:
        result = '('
        result += dfs(v)
        result += ')'

        for i in range(1, len(u)-1):
            if(u[i]=='('):
                result += ')'
            else:
                result += '('
    return result

def solution(p):
    answer = dfs(p)
    return answer
print(solution("()))((()"))