class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, num in enumerate(nums):
            if num > 0:
                break
            
            l = i + 1
            r = len(nums) - 1

            while l < r:
                if num + nums[l] + nums[r] == 0:
                    res.append([num, nums[l], nums[r]])
                    break
                elif num + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    l += 1
                
        
        return res