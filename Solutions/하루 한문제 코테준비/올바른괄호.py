def solution(s):
    answer = True
    stack = []
    for i in s:
        if(i==')'):
            if(len(stack) == 0 or stack.pop(-1) != '('):
                answer = False
                break
        else:
            stack.append(i)
        
    return answer and len(stack) == 0

print(solution((")()(")))