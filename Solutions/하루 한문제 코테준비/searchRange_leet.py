def searchRange(self, nums: List[int], target: int) -> List[int]:
        start,end = 0, len(nums)-1
        result = [-1,-1]
        while(start<=end):
            mid = (start+end)//2
            if(nums[mid]==target and nums[mid-1] != target):
                result[0] = mid
                break
            if(nums[mid]>=target):
                end = mid - 1
            else:
                start = mid + 1
        start,end = 0, len(nums)-1
        while(start<=end):
            mid = (start+end)//2
            if(nums[mid]==target and nums[mid+1] != target):
                result[1] = mid
                break
            if(nums[mid]>=target):
                end = mid - 1
            else:
                start = mid + 1
        return result