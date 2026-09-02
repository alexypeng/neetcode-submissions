from heapq import heapify, heappop, heappush

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        elif not stones:
            return 0
        neg = [-s for s in stones]
        heapify(neg)

        while len(neg) > 2:
            heaviest = -heappop(neg)
            second = -heappop(neg)

            heappush(neg, -(heaviest - second))
        
        return -heappop(neg) + heappop(neg)