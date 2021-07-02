import itertools
def check(n):
    if n <= 1:
        return False
    if n <= 2:
        return True
    else:
        for i in range(2,n):
            if n%i == 0:
                return False

    return True

def solution(numbers):

    answer = []
    for j in range(1,len(numbers)+1):
        per = list(map(''.join, itertools.permutations(numbers,j)))
        per = set(per)
        for i in per:
            p = int(i)
            if check(p):
                answer.append(p)
    print(answer)
    answer = set(answer)
    return len(answer)

print(solution("17"))