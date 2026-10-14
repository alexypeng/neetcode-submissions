class MedianFinder:

    def __init__(self):
        self.minHeap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.minHeap, num)

    def findMedian(self) -> float:
        total_len = len(self.minHeap)
        if total_len % 2 == 0:
            return (self.minHeap[total_len // 2] + self.minHeap[total_len // 2 - 1]) / 2
        return self.minHeap[total_len // 2]