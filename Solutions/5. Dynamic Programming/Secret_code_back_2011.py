num = input()
length = len(num)
d = [1 for i in range(length+1)] # 0부터 길이까지 가능한 경우의 수를 기록하는 리스트

if int(num[0]) == 0: # 맨앞이 0으로 시작하면 암호가 될수 없음
    print(0)
    exit(0)
if length == 1: # 길이가 1이면 암호가 될수 있는 경우는 1개 뿐임
    print(1)
    exit(0)

for i in range(2,length+1): # 2번째 수부터 판단, d 맨앞에 길이가 0일때 추가해주어서 현재숫자값은 i-1임
    if int(num[i-1]) == 0: # 현재숫자가 0이고
        if 0<int(num[i-2]+num[i-1])<=26: # 이전과 합친 숫자가 범위안에 있을때
            d[i] = d[i-2] # 두번째 전거 그대로
        else: # 범위안에 없으면
            d[i] = 0 # 경우의수는 0
        continue

    if int(num[i-2]) == 0: # 이전 숫자의 값이 0일때
        d[i] = d[i-1] # 이전 경우의 수 그대로 가져옴
        continue

    # 현재, 이전에 0이 포함되어 있지 않은 경우
    if 0<int(num[i-2]+num[i-1])<=26: # 이전과 합친 숫자가 범위안에 있으면
        d[i] = d[i-2]+d[i-1] # 2개전 + 1개전
    else: # 범위 벗어나면
        d[i] = d[i-1] # 이전값 그대로 가져옴

# print(d)
print(d[length]%1000000)
