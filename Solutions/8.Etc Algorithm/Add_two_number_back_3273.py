n = int(input())
number= list(map(int, input().split(" ")))
match = int(input())

number.sort() # 정렬을 해줘야 투포인트 사용할 수 있음

count = 0
end = n-1
intervel_sum = 0
start = 0

while start < end: #  두 포인트가 엇갈릴때 까지
    intervel_sum = number[start]+number[end] # 두수의합
    if intervel_sum == match: # 찾는 수랑 같아 질때
        count += 1 # 개수 카운트
        start += 1 # 한 칸 옮겨주기
    if intervel_sum < match: # 합이 더 작을때
        start += 1 # 앞에거를 한칸뒤로
        continue
    else: # 합이 더 클때
        end -= 1 # 뒤에꺼를 한칸 앞으로

print(count)