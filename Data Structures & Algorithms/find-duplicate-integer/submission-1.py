class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0

        while slow == 0 or slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        start = 0
        while start != slow:
            slow = nums[slow]
            start = nums[start]
        
        return slow