def maxArea(self, height: List[int]) -> int:
        start,end = 0,len(height)-1
        result = 0
        while(start<end):
            h_start, h_end = height[start],height[end]
            result = max((end-start)*min(h_start, h_end),result)
            if(h_start<h_end):
                start += 1
            else:
                end -= 1
        return result