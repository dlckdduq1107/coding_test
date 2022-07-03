import re

# Trie구조를 사용해서 풀어야 함 정규식 사용하면 효율성에서 실패함
def solution(words, queries):
    answer = []
    for each in queries:
        q_num = list(each).count("?")
        q_re = re.compile('[?]+')
        sub = q_re.findall(each)[0]
        re_each = each.replace(sub,'.{%s}' %q_num)
        q = re.compile(re_each)

        total=0
        for w in words:
            res = q.findall(w)
            if(len(res)!=0 and len(res[0])==len(w)):
                total += 1
            # print(res, re_each)
        answer.append(total)
    return answer

print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))