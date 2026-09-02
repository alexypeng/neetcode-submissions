class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = []

        for x, y in points:
            heapq.heappush(pq, (math.sqrt(x**2 + y**2), [x, y]))
        
        res = []

        for _ in range(k):
            res.append(heapq.heappop(pq)[1])

        return res