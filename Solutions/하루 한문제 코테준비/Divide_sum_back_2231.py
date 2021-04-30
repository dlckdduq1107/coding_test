n = int(input())#입력

for i in range(n): # 입력된 범위까지 반복
    n_list = [] # 숫자, 각자리 숫자들 저장 리스트
    n_list.append(i) # 생성자가 될 숫자 추가
    for j in str(i): # 문자열로 바꾼다음 각자리 숫자에 대해 반복
        n_list.append(int(j)) # 각자리 숫자 리스트에 추가
    if sum(n_list) == n: # 숫자 + 각 자리 숫자의 합이 입력된 값과 같으면
        print(i) # 출력하고
        exit(0) # 종료
print(0) # 생성자가 없을경우 0출력
