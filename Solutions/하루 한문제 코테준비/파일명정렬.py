import re
def solution(files):
    result = []
    p = re.compile('[0-9]+')
    for each_file in files:
        m = p.search(each_file)
        num = m[0]
        origin_head = each_file[:m.start()]
        head = origin_head.upper()
        tail = each_file[m.end():]
        print(each_file, head,num,tail)
        result.append([head,num,tail,origin_head])
    
    result.sort(key=lambda x:int(x[1]))
    result.sort(key=lambda x:x[0])
    answer = []
    for i in result:
        answer.append(i[3]+i[1]+i[2])
    return answer
print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))