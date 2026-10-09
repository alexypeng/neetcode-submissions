class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index = len(nums) // 2
        while nums:
            mid = len(nums) // 2
            if target == nums[mid]:
                return index
            elif target > nums[mid]:
                index += mid
                nums = nums[mid + 1:]
            else:
                index -= mid
                nums = nums[:mid]
            
        
        return -1