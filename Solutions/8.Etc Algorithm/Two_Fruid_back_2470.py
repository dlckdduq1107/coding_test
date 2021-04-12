n = int(input())
number = list(map(int,input().split(" ")))
number.sort() # 정렬

start,end = 0,n-1 # 양쪽에서 좁혀오는 형태

result = number[start]+number[end] # 양쪽에서 좁혀오므로 처음 값은 양쪽을 더한 값으로
a,b = start,end # 시작과 끝으로 설정
while start < end: # 엇갈릴때 까지
    temp = number[start]+number[end] # 두개 더한거
    if abs(temp) < abs(result): # 더 0에 가까운거 찾았을때
        result = temp # 결과를 저장하고
        a = start  # 위치도 저장
        b = end

    if temp == 0: # 0일때 가장 작으므로 바로 탈출
        break
    elif temp>0: # 양수이면 오른쪽이 더 크므로 오른쪽을 한칸 줄여줌
        end -= 1
    else: # 음수이면 왼쪽이 더 크므로 왼쪽을 한칸 줄여줌
        start += 1

print(number[a],number[b])