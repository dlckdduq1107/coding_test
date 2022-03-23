def solution(n, left, right):
    answer = []
    left,rigjt = long(left),long(right)
    for i in range(left,right+1):
        answer.append(max(i//n,i%n)+1)
    return answer