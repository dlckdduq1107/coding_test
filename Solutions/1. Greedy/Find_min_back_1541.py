minus_list = list(input().split("-")) # 마이너스로 먼저 나눠줌
dup_list = minus_list # 리스트 복사

for plus in minus_list: # 플러스를 먼저 더함
    if '+' in plus: # 플러스를 더하고 복사한 리스트를 수정함
        res_plus_list = list(map(int,plus.split("+")))
        res_plus = sum(res_plus_list)
        dup_list[minus_list.index(plus)] = res_plus

dup_list = list(map(int, dup_list)) # 리스트 int형 변환

print(dup_list[0]-sum(dup_list[1:])) # 첫번째 -(나머지 합)