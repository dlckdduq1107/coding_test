def solution(answers):
    result = [0,0,0]
    answer = []
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]
    for i in range(len(answers)):
        if(a[i%5]==answers[i]):
            result[0] += 1
        if(b[i%len(b)]==answers[i]):
            result[1] += 1
        if(c[i%len(c)]==answers[i]):
            result[2] += 1
    m = max(result)
    for i in range(len(result)):
        if(result[i]==m):
            answer.append(i+1)

    return answer