class Solution:
    def maxArea(self, heights: List[int]) -> int:
        hi = 0

        l = 0
        r = len(heights) - 1
        while l < r:
            area = (r - l) * min(heights[r], heights[l])
            hi = max(hi, area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return hi