class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)

        hi = 0

        for num in nums:
            if num - 1 not in nums:
                count = 0
                temp = num
                while temp in nums:
                    count += 1
                    temp += 1
                hi = max(hi, count)

        return hi