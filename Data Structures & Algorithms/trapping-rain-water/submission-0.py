class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = [0] * n
        right = [0] * n

        hi = 0
        for i in range(n):
            left[i] = hi
            hi = max(hi, height[i])

        hi = 0
        for i in range(n-1, -1, -1):
            right[i] = hi
            hi = max(hi, height[i])
        
        res = 0

        for i in range(n):
            res += max(0, min(left[i], right[i]) - height[i])

        return res