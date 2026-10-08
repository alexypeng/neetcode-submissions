class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxheap = []
        res = []

        for end in range(len(nums)):
            if maxheap and end - maxheap[0][1] + 1 > k:
                heapq.heappop_max(maxheap)

            while maxheap and nums[end] >= maxheap[-1][0]:
                maxheap.pop()

            heapq.heappush_max(maxheap, (nums[end], end))
            
            if end >= k - 1:
                res.append(maxheap[0][0])
        
        return res