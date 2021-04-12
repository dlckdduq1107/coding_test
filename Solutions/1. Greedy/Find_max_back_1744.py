n = int(input())
plus_list = []
minus_list = []
result = 0

for i in range(n): # 입력 값을 음수 양수로 나누어 리스트에 넣음
    data = int(input())
    if data > 0: # 양수 리스트
        if data == 1: # 1일때는 묶지 않으므로 미리 더해줌
            result += 1
        else:
            plus_list.append(data)
    elif data <= 0: # 음수 리스트
        minus_list.append(data)

plus_list.sort(reverse = True) # 큰수부터 정렬
minus_list.sort() # 작은수 부터 정렬

for i in range(0,len(plus_list),2): # 양수리스트 두개 씩 묶음
    if (i+1) >= len(plus_list): # 남은개수가 자신 혼자일때
        result += plus_list[i]
    else:
        result += plus_list[i]*plus_list[i+1]

for j in range(0,len(minus_list),2): # 음수 리스트 두개 씩 묶음, 0 문제는 자동적으로 해결
    if (j+1) >= len(minus_list): # 남은개수가 자신 혼자일때
        result += minus_list[j]
    else:
        result += minus_list[j]*minus_list[j+1]

print(result)
