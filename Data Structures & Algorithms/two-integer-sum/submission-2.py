class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(nums):
            if target - num in seen:
                return [min(i, seen[target - num]), max(i, seen[target - num])]
            seen[num] = i
        
        return [0, 0]