import heapq
class MedianFinder:

    def __init__(self):
        self.heap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.heap, num)

    def findMedian(self) -> float:
        n = len(self.heap)
        self.heap.sort()
        if n % 2:
            return self.heap[n//2]
        
        return (self.heap[n//2] + self.heap[(n//2) - 1]) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()