class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minDp = [float('inf')] * len(nums)
        maxDp = [float('-inf')] * len(nums)

        minDp[-1] = nums[-1]
        maxDp[-1] = nums[-1]
        res = float('-inf')

        for i in range(len(nums) - 2, -1, -1):
            minDp[i] = min(nums[i], minDp[i+1] * nums[i], maxDp[i+1] * nums[i])
            maxDp[i] = max(nums[i], minDp[i+1] * nums[i], maxDp[i+1] * nums[i])
            res = max(res, maxDp[i])
        
        return res