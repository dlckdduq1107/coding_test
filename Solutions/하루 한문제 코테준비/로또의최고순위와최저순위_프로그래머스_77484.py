def solution(lottos, win_nums):
    result = {6:1,5:2,4:3,3:4,2:5,1:6,0:6}
    answer = []
    temp = 0
    zero = 0
    for i in lottos:
        if(i in win_nums):
            temp += 1
        elif(i == 0):
            zero += 1

    answer.append(result[temp+zero])
    answer.append(result[temp])
    return answer

print(solution([44, 1, 0, 0, 31, 25],[31, 10, 45, 1, 6, 19]))