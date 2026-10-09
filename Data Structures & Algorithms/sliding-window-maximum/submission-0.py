class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxheap = []
        res = []

        for end in range(len(nums)):
            while maxheap and nums[end] >= maxheap[0][0]:
                heapq.heappop(maxheap)
            heapq.heappush_max(maxheap, (nums[end], end))
            
            if end - maxheap[0][1] + 1 > k:
                maxheap.pop(0)
            
            if end >= k - 1:
                res.append(maxheap[0][0])
        
        return res