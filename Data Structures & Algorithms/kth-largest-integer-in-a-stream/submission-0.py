class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = []

        for num in nums:
            heapq.heappush_max(self.min_heap, num)

    def add(self, val: int) -> int:
        heapq.heappush_max(self.min_heap, val)

        readd = []

        for _ in range(self.k):
            popped = heapq.heappop_max(self.min_heap)
            readd.append(popped)

        for elem in readd:
            heapq.heappush_max(self.min_heap, elem)

        return popped