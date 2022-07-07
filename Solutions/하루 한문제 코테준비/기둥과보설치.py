def check(result):
    for x,y,t in result:
        if(t==0):
            if(y==0 or ([x-1,y,1] in result) or ([x,y,1] in result) or ([x,y-1,0] in result)):
                continue
            return False
        else:
            if(([x,y-1,0] in result) or ([x+1,y-1,0] in result) or (([x-1,y,1] in result) and ([x+1,y,1] in result))):
                continue
            return False
    return True

def solution(n, build_frame):
    answer = []
    for x,y,t,build in build_frame:
        if(build):
            answer.append([x,y,t])
            if(not check(answer)):
                answer.remove([x,y,t])
        else:
            answer.remove([x,y,t])
            if(not check(answer)):
                answer.append([x,y,t])
    answer.sort(key=lambda x:x[2])
    answer.sort(key=lambda x:x[1])
    answer.sort(key=lambda x:x[0])

    return answer
print(solution(5,[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))