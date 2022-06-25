from itertools import combinations
def solution(relation):
    answer = 0
    total = len(relation)
    res = [] 
    for i in range(1,5):
        for j in combinations(range(4),i):
            temp = []
            
            print(j)
    return answer
print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))