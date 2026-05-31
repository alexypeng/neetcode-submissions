class Solution:
    def maxArea(self, heights: List[int]) -> int:
        hi = 0
        l = 0
        r = len(heights) - 1

        while l < r:
            h = min(heights[l], heights[r])
            a = h * (r - l)
            hi = max(a, hi)

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        
        return hi