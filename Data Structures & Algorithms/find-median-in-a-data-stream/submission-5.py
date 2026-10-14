class MedianFinder:

    def __init__(self):
        self.small_heap = []
        self.large_heap = []

    def addNum(self, num: int) -> None:
        if not self.small_heap:
            heapq.heappush_max(self.small_heap, num)
            return
        if not self.large_heap:
            left = heapq.heappop_max(self.small_heap)
            heapq.heappush_max(self.small_heap, min(left, num))
            heapq.heappush(self.large_heap, max(left, num))
            return

        left = heapq.heappop_max(self.small_heap)
        right = heapq.heappop(self.large_heap)

        if (len(self.small_heap) + len(self.large_heap)) % 2 == 0:
            heapq.heappush_max(self.small_heap, left)
            heapq.heappush_max(self.small_heap, min(right, num))
            heapq.heappush(self.large_heap, max(right, num))
        else:
            heapq.heappush_max(self.small_heap, min(left, num))
            heapq.heappush(self.large_heap, max(left, num))
            heapq.heappush(self.large_heap, right)

    def findMedian(self) -> float:
        if (len(self.small_heap) + len(self.large_heap)) % 2:
            return self.small_heap[0]
        return (self.small_heap[0] + self.large_heap[0]) / 2