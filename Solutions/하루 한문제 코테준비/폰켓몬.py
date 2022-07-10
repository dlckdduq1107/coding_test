def solution(nums):
    answer = 0
    result = set()
    for i in nums:
        result.add(i)
    if(len(result)<=len(nums)/2):
        answer = len(result)
    else:
        answer = len(nums)/2
    return answer

    