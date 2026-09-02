class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        neg = []
        for num in nums:
            heapq.heappush(neg, -num)

        res = 0

        for i in range(k):
            res = -heapq.heappop(neg)
        
        return res