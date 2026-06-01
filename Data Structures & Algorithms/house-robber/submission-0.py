class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * len(nums)

        for i in range(len(nums)):
            if i < 2:
                dp[i] = nums[i]
                continue
            
            dp[i] = nums[i] + max(dp[:i-1])
        
        return max(dp)
