class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [(math.sqrt(x ** 2 + y ** 2), x, y) for x, y in points]

        heapq.heapify(distances)
        res = []

        for _ in range(k):
            point = heapq.heappop(distances)
            x, y, = point[1], point[2]

            res.append((x, y))

        return res