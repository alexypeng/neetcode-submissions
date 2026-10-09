class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            m = l + ((r - l) // 2)
            
            if nums[m] >= nums[l]:
                if nums[m] < nums[r]:
                    r = m
                else:
                    l = m
            else:
                if nums[m] >= nums[m - 1]:
                    r = m
                else:
                    l = m
        
        return nums[l]