n = int(input())
count = 0

for i in range(1,n+1):
    if 0<i<100: # 두자리 숫자까지는 차이를 비교할게 없으므로 카운트
        count += 1
    elif 100<=i<1000: # 세자리 숫자 일때
        differ = int(str(i)[0]) - int(str(i)[1]) # 첫번째와 두번쟤의 차이
        if differ == int(str(i)[1]) - int(str(i)[2]): # 공차가 같을때
            count += 1
print(count)