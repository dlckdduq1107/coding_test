from collections import defaultdict
def solution(A):
    nums = defaultdict(list)
    for idx,i in enumerate(A):
        nums[i].append(idx)
    res = []
    for i in nums:
        if(len(A)/2<len(nums[i])):
            res = nums[i]
    if(res == []):
        return -1
    else:
        return res[0]
    