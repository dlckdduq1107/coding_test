import re
dup = re.compile('([a-z0-9-_.]+)') # 소문자,숫자,특수문자 정규식


id = input().lower() # 소문자로
m = dup.findall(id) # 정규식에 맞는 부분을 모두 찾아 리스트로 리턴
id = "".join(m) # 합침
#print(m)

conti = re.compile('([.]{2,})') # .이 2번 이상 반복되는 경우의 정규식
m = conti.findall(id)
for i in m: # 매칭되는 부분 반복
    id = id.replace(i,".",1) # 문자열 대체 마지막 1은 치환할 개수(없으면 해당 되는 모든거 치환함)
#print(id)

first_dot_check = re.compile('(^[.]+)|([.]+$)') # 맨앞과 맨끛에 . 있는지 체크
id = first_dot_check.sub("",id) # 치환

#print(id)
if(id == ""):
    id = "a"

if(len(id)>=16): # 길이 16이상일때
    id = id[:15]
    id = first_dot_check.sub("",id)
if(len(id)<=2):
    last = id[-1]
    while(len(id)!=3):
        id += last

print(id)