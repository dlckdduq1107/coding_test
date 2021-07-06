def solution(brown, yellow):
    answer = []
    yac= []
     ##24이면 [1,2,3,4,6,8,12,24]로 약수구하고 양쪽에서부터 가로,세로를 설정한다음 조건 맞는지 체크
    for i in range(1,yellow+1): # 약수구하고
        if yellow%i == 0:
            yac.append(i)

    for i in range(len(yac)//2+1): # 차례대로 검사
        if (yac[i]+2)*(yac[-1-i]+2)-yellow == brown: # 전체 개수-노란색이 갈색이면
            answer.append(yac[-1-i]+2)
            answer.append(yac[i]+2)
            break
    return answer


print(solution(10,2))