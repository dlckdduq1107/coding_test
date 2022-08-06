import re
def basic_score(word, target):
    res = 0
    q = re.compile("[a-z]+")
    for i in q.findall(target):
        if(word==i):
            res += 1
    return res

def solution(word, pages):
    answer = 0
    score = {}
    title_wrapper = re.compile("<meta property=\"og:url\" content=\"([a-z:/\.]+)\"/>")
    title = re.compile("https:[a-z:\/.]+")
    for i,each in enumerate(pages):
        re_title = title_wrapper.search(each.lower())[0]
        score[title.search(re_title)[0]] = {"index":i, "origin":each.lower()}
    for i in score:
        score[i]["basic"] = basic_score(word.lower(),score[i]["origin"])
    # print(score)
    for i in score:
        q = re.compile("<a href=\"https://[a-z./]+\">")
        score[i]["out_link_total"] = 0
        score[i]["out_link_list"] = []
        for j in q.findall(score[i]["origin"]):
            e = re.compile("https:[a-z:\/.]+")
            out_link = e.search(j)[0]
            score[i]["out_link_total"] += 1
            score[i]["out_link_list"].append(out_link)
    for i in score:
        for j in score[i]["out_link_list"]:
            if(j not in score):
                continue
            if("link_score" not in score[j]):
                score[j]["link_score"] = 0
            score[j]["link_score"] += score[i]["basic"]/score[i]["out_link_total"]
    # print(score)
    res = []
    for i in score:
        link_score = 0 if "link_score" not in score[i] else score[i]["link_score"]
        res.append([score[i]["basic"]+link_score,score[i]["index"]])
    res.sort(reverse=True)
    # print(res)
    return res[0][1]
print(solution("Muzi",["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]))