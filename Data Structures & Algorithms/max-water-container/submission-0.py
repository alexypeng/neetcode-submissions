class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxW = 0
        l, r = 0, len(heights) - 1

        while l < r:
            width = r - l
            height = min(heights[r], heights[l])
            maxW = max(width * height, maxW)

            if heights[r] > heights[l]:
                l += 1
            else:
                r -= 1
        
        return maxW
        